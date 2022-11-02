from django.forms import ModelForm
from django import forms
from fh.models import fh

class Formfh(ModelForm):
    class Meta:
        model = fh
        fields = ['judul', 'jurusan', 'ketua jurusan']

        widgets = {
            'judul' : forms.TextInput({'class':'form-control'})}
    'jurusan' : forms.Select({'class':'form-control'})
    'ketua jurusan' : forms.TextInput({'class':'form-control'})
