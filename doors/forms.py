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


type_choice = [('металл/металл','металл/металл'),('металл/панель','металл/панель'),('панель/панель','панель/панель'),('None','None')]
lock_choice = [('два','два'),('один','один'),('None','None')]
color_inside_choice = [('белый','белый'),('светлый','светлый'),('темный','темный'),('None','None')]
style_choice = [('классика','классика'),('модерн','модерн'),('неоклассика','неоклассика'),('None','None')]
features_choice = [('замки Kale','замки Kale'),('с зеркалом','с зеркалом'),('тамбурные','тамбурные'),('уличные','уличные'),('утепленная коробка','утепленная коробка'),('черное стекло','черное стекло'),('None','None')]
color_outside_choice = [('белый','белый'),('темный','темный'),('черный','черный'),('None','None')]
price_scale_choice = [('По умолчанию','По умолчанию'),('Сначала дешевле','Сначала дешевле'),('Сначала дороже','Сначала дороже'),('None','None')]
class filter_metal(forms.Form):
    type = forms.TypedChoiceField(choices=type_choice,coerce = str)
    lock = forms.TypedChoiceField(choices=lock_choice,coerce = str)
    color_inside = forms.TypedChoiceField(choices=color_inside_choice,coerce = str)
    style = forms.TypedChoiceField(choices=style_choice,coerce = str)
    features = forms.TypedChoiceField(choices=features_choice,coerce = str)
    color_outside = forms.TypedChoiceField(choices=color_outside_choice,coerce = str)
    price_scale = forms.TypedChoiceField(choices=price_scale_choice,coerce = str)