from .models import categoriesImport, measure
from django import forms

class categories_forms(forms.ModelForm):
    class Meta:
        model = categoriesImport
        fields = ['id','json_file']

class SearchForm(forms.Form):
    query = forms.CharField(max_length= 250)

class measureForm(forms.ModelForm):
    class Meta:
        model = measure
        fields = ['name','number','e_mail','address']


type_choice = ['металл/металл','металл/панель','панель/панель']
lock_choice = ['два','один']
color_inside_choice = ['белый','светлый','темный']
style_choice = ['классика','модерн','неоклассика']
features_choice = ['замки Kale','с зеркалом','тамбурные','уличные','утепленная коробка','черное стекло']
color_outside_choice = ['белый','темный','черный']
price_scale_choice = ['По умолчанию','Сначала дешевле','Сначала дороже']
class filter_metal(forms.Form):
    type = forms.ChoiceField(choices=type_choice)
    lock = forms.ChoiceField(choices=lock_choice)
    color_inside = forms.ChoiceField(choices=color_inside_choice)
    style = forms.ChoiceField(choices=style_choice)
    features = forms.ChoiceField(choices=features_choice)
    color_outside = forms.ChoiceField(choices=color_outside_choice)
    price_scale = forms.ChoiceField(choices=price_scale_choice)