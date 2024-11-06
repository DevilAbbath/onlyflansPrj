from django import forms
from .models import ContactForm, Comentary

class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']


class ComentaryForm(forms.ModelForm):
    class Meta:
        model = Comentary
        fields = ['txt']