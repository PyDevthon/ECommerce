from django import forms
from .models import Contact
from django.contrib.auth.forms import AuthenticationForm


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('product',)
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'phone': forms.TextInput(attrs={'class': 'form-control', 'pattern': "[1-9]{1}[0-9]{9}",
                                                   'placeholder': 'Enter 10 digit Phone Number'}),
                   'comments': forms.Textarea(attrs={'class': 'form-control'})}


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
