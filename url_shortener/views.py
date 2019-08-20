from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Url
from .forms import UrlForm
import string
import random


def RedirectShorturl(request, shortname):
    try:
        url = Url.objects.get(shortname=shortname)
        return redirect(url.url)
    except:
        return render(request,template_name='url_shortener/404.html')


def GetUrls(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            shortname = form.cleaned_data['CustomUrl']
            if shortname == '':
                shortname = generator()
                mainurl = form.cleaned_data['MainUrl']
                url = Url(url=mainurl,shortname=shortname)
                url.save()
                messages.success(request,'ShortUrl was Created!')
                return render(request,'url_shortener/shorturl_created.html',{'mainurl' : mainurl,'shortname' : shortname,})
            else:
                try:
                    url = Url(url=form.cleaned_data['MainUrl'],shortname=shortname)
                    url.save()
                    messages.success(request,'ShortUrl was Created!')
                    return render(request,'url_shortener/shorturl_created.html',{'mainurl' : form.cleaned_data['MainUrl'],'shortname' : shortname,})
                except:
                    messages.info(request,'Url is already taken. Try with different name.')
                    return redirect('home')

    form = UrlForm()
    return render(request,'url_shortener/url_short.html',{'form':form})

def generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

