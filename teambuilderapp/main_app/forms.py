from django import forms
from .models import Trophy

class TrophyForm(forms.ModelForm):
    class Meta:
        model = Trophy
        fields = ('trophy',)