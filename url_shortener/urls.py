from django.urls import path
from . import views

urlpatterns = [
    path('<shortname>/',views.RedirectShorturl),
    path('',views.GetUrls,name='home')
]
