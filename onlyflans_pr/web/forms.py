from django import forms
from .models import Testimonio


class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label="Nombre")
    message = forms.CharField(widget=forms.Textarea, label="Mensaje")
    

class TestimonioForm(forms.ModelForm):
    class Meta:
        model = Testimonio
        fields = ['testimonio', 'calificacion']
