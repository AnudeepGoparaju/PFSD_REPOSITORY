from django import forms
from .models import *
class MemberForm(forms.ModelForm):
    class Meta:
        model=users
        fields=['name','email','password','age','balance']

class FForm(forms.ModelForm):
    class Meta:
        model=feed
        fields=['feedb']

