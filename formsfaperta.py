from django.forms import ModelForm
from django import forms
from faperta.models import faperta

class Formfaperta(ModelForm):
    class Meta:
        model = faperta
        fields = ['judul', 'jurusan', 'ketua jurusan']

        widgets = {
            'judul' : forms.TextInput({'class':'form-control'})}
    'jurusan' : forms.Select({'class':'form-control'})
    'ketua jurusan' : forms.TextInput({'class':'form-control'})
