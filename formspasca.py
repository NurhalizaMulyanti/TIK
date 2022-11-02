from django.forms import ModelForm
from django import forms
from pascasarjana.models import pascasarjana

class Formpascasarjana(ModelForm):
    class Meta:
        model = pascasarjana
        fields = ['judul', 'jurusan', 'ketua jurusan']

        widgets = {
            'judul' : forms.TextInput({'class':'form-control'})}
    'jurusan' : forms.Select({'class':'form-control'})
    'ketua jurusan' : forms.TextInput({'class':'form-control'})
