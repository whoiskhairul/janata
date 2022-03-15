from django import forms
from load_data.models import ReadCSV

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=100)
    file = forms.FileField()

