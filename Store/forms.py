from  django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('product', )
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'phone': forms.TextInput(attrs={'class': 'form-control', 'pattern': "[1-9]{1}[0-9]{9}",
                                                   'placeholder': 'Enter 10 digit Phone Number'}),
                   'comments': forms.Textarea(attrs={'class': 'form-control'})}
