from django.shortcuts import render,redirect
from .models import Url

def RedirectShorturl(request, shortname):
    try:
        url = Url.objects.get(shortname=shortname)
        return redirect(url.url)
    except:
        return render(request,template_name='url_shortener/404.html')
