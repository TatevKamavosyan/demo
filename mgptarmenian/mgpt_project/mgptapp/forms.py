# textprocessor/forms.py
from django import forms
from .models import Text

class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ['input_text']
