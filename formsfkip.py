from django.forms import ModelForm
from django import forms
from fkip.models import fkip

class Formfkip(ModelForm):
    class Meta:
        model = fkip
        fields = ['judul', 'jurusan', 'ketua jurusan']

        widgets = {
            'judul' : forms.TextInput({'class':'form-control'})}
    'jurusan' : forms.Select({'class':'form-control'})
    'ketua jurusan' : forms.TextInput({'class':'form-control'})
