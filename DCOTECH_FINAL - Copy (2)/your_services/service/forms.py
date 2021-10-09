from django import forms
from django.db.models import fields
from django.forms.widgets import Textarea
from .models import *
from django.forms import ModelForm

class nameForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','body','cover'] 

   
    
class comment(forms.Form):
    querry=forms.CharField(widget=Textarea)

class search_form(forms.Form):
    search=forms.CharField(required=False)
    search_in=forms.ChoiceField(required=False,choices=(('tittle','title'),('contributer','contributer')))