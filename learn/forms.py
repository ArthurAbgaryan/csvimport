from django import forms
from .models import BookImport,CatalogImport

class CatalogImportForm(forms.ModelForm):
    class Meta:
        model = CatalogImport
        fields = ('json_file',)

class BookImportForm(forms.ModelForm):
    class Meta:
        model = BookImport
        fields = ('csv_file',)