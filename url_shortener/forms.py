from  django import forms

class UrlForm(forms.Form):
    MainUrl = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter url you want to short'}))
    CustomUrl = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter name you want as suffix to shorturl'}),required=False)
