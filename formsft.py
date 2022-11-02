from django.forms import ModelForm
from django import forms
from ft.models import ft

class Formft(ModelForm):
    class Meta:
        model = ft
        fields = ['judul', 'jurusan', 'ketua jurusan']

        widgets = {
            'judul' : forms.TextInput({'class':'form-control'})}
    'jurusan' : forms.Select({'class':'form-control'})
    'ketua jurusan' : forms.TextInput({'class':'form-control'})
