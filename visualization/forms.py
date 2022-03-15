from dataclasses import fields
from django import forms
from load_data.models import ReadCSV


class EditReadCSVForm(forms.ModelForm):
    class Meta:
        model = ReadCSV
        fields = '__all__'
    