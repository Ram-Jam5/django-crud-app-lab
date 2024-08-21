from django import forms
from .models import Trophy

class TrohpyForm(forms.ModelForm):
    class Meta:
        model = Trophy
        fields = ('TROPHIES',)