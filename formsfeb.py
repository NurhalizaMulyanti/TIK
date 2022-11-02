from django.forms import ModelForm
from django import forms
from feb.models import feb

class Formfeb(ModelForm):
    class Meta:
        model = feb
        fields = ['judul', 'jurusan', 'ketua jurusan']

        widgets = {
            'judul' : forms.TextInput({'class':'form-control'})}
    'jurusan' : forms.Select({'class':'form-control'})
    'ketua jurusan' : forms.TextInput({'class':'form-control'})
