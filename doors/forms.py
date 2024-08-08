from .models import categoriesImport
from django import forms

class categories_forms(forms.ModelForm):
    class Meta:
        model = categoriesImport
        fields = ['id','json_file']