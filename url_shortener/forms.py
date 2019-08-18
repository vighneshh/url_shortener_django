from  django import forms

class UrlForm(forms.Form):
    MainUrl = forms.CharField()
    CustomUrl = forms.CharField(required=False)
