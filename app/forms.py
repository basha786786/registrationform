from django import forms
from django.forms import widgets
from app.models import *
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}
class profileForm(forms.ModelForm):
    class Meta:
        model=profile
        fields=['address','profile_pic']