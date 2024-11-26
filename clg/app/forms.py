from django import forms
from .models import *

class course_form(forms.Form):
    name=forms.CharField()
    phone=forms.IntegerField()
    email=forms.EmailField()
    message=forms.CharField()
    coursee=forms.CharField()