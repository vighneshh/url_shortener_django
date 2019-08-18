from django.shortcuts import render,redirect
from .models import Url
from .forms import UrlForm

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
            customurl = form.cleaned_data['CustomUrl']
            print(customurl)
    form = UrlForm()
    return render(request,'url_shortener/url_short.html',{'form':form})

