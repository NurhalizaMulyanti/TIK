from django.forms import ModelForm
from django import forms
from fisip.models import fisip

class Formfisip(ModelForm):
    class Meta:
        model = fisip
        fields = ['judul', 'jurusan', 'ketua jurusan']

        widgets = {
            'judul' : forms.TextInput({'class':'form-control'})}
    'jurusan' : forms.Select({'class':'form-control'})
    'ketua jurusan' : forms.TextInput({'class':'form-control'})
