from django import forms
from .models import CreateArtist

class CreateArtistForm(forms.ModelForm):
    class Meta:
        model = CreateArtist
        fields = '__all__'