from django import forms

class UserRegistrationForm(forms.Form):
  username = forms.forms.CharField()
  email = forms.EmailField()
  password = forms.forms.CharField()