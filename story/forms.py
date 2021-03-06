from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    contact_number = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    message = forms.CharField(widget=forms.Textarea, max_length=1000)