from django.forms import ModelForm
from django import forms
from fk.models import fk

class Formfk(ModelForm):
    class Meta:
        model = fk
        fields = ['judul', 'jurusan', 'ketua jurusan']

        widgets = {
            'judul' : forms.TextInput({'class':'form-control'})}
    'jurusan' : forms.Select({'class':'form-control'})
    'ketua jurusan' : forms.TextInput({'class':'form-control'})
