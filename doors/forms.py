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

#Форма для фильтра металлических дверей
type_choice = [('--','Тип'),('металл/металл','металл/металл'),('металл/панель','металл/панель'),('панель/панель','панель/панель')]
lock_choice = [('--','Замки'),('два','два'),('один','один')]
color_inside_choice = [('--','Цвет изнутри'),('белый','белый'),('светлый','светлый'),('темный','темный')]
style_choice = [('--','Стиль'),('классика','классика'),('модерн','модерн'),('неоклассика','неоклассика')]
features_choice = [('--','Особенности'),('замки Kale','замки Kale'),('с зеркалом','с зеркалом'),('тамбурные','тамбурные'),('уличные','уличные'),('утепленная коробка','утепленная коробка'),('черное стекло','черное стекло')]
color_outside_choice = [('--','Цвет снаружи'),('белый','белый'),('темный','темный'),('черный','черный')]
price_scale_choice = [('--','По умолчанию'),('Сначала дешевле','Сначала дешевле'),('Сначала дороже','Сначала дороже')]
class filter_metal(forms.Form):
    type = forms.TypedChoiceField(choices=type_choice,coerce = str)
    lock = forms.TypedChoiceField(choices=lock_choice,coerce = str)
    color_inside = forms.TypedChoiceField(choices=color_inside_choice,coerce = str)
    style = forms.TypedChoiceField(choices=style_choice,coerce = str)
    features = forms.TypedChoiceField(choices=features_choice,coerce = str)
    color_outside = forms.TypedChoiceField(choices=color_outside_choice,coerce = str)
    price_scale = forms.TypedChoiceField(choices=price_scale_choice,coerce = str)
#Конец  Форма для фильтра металлических дверей


#Форма для фильтра межкомнатных дверей
view_choice = [('--','Тип'),('рамочные','рамочные'),('щитовые','щитовые')]
type_choice_1 = [('--','Вид'),('глухие','глухие'),('остекленные','остекленные')]
color_choice = [('--','Цвет'),('белый','белый'),('светлый','светлый'),('темный','темный')]
style_choice_1 = [('--','Стиль'),('классика','классика'),('модерн','модерн'),('минимализм','минимализм'),('неоклассика','неоклассика')]
features_choice_1 = [('--','Особенности'),('painted wood','painted wood'),('объемная филенка','объемная филенка'),('с зеркалом','с зеркалом'),('черный декор','черный декор')]
# status_choice = [('--','Статус'),('белый','белый'),('темный','темный'),('черный','черный')]
price_scale_choice = [('--','По умолчанию'),('По умолчанию','По умолчанию'),('Сначала дешевле','Сначала дешевле'),('Сначала дороже','Сначала дороже')]
class filter_wood(forms.Form):
    view_w = forms.TypedChoiceField(choices=view_choice,coerce = str)
    type = forms.TypedChoiceField(choices=type_choice_1,coerce = str)
    color = forms.TypedChoiceField(choices=color_choice,coerce = str)
    style = forms.TypedChoiceField(choices=style_choice_1,coerce = str)
    features_1 = forms.TypedChoiceField(choices=features_choice_1,coerce = str)
    # status = forms.TypedChoiceField(choices=status_choice,coerce = str)
    price_scale = forms.TypedChoiceField(choices=price_scale_choice,coerce = str)


#Конец Форма для фильтра межкомнатных дверей

#Начало форма для складных дверей
view_sk = [('--','Тип'),('глухие','глухие'),('остекленные','остекленные')]
color_sk = [('--','Цвет'),('белый','белый'),('светлый','светлый'),('темный','темный')]
style_sk = [('--','Стиль'),('модерн','модерн'),('минимализм','минимализм')]
class filter_sk(forms.Form):
    view_sk = forms.TypedChoiceField(choices=view_sk,coerce = str)
    color_sk = forms.TypedChoiceField(choices=color_sk,coerce = str)
    style_sk = forms.TypedChoiceField(choices=style_sk,coerce = str)
    price_scale_sk = forms.TypedChoiceField(choices=price_scale_choice,coerce = str)
#Конец формы для складных дверей

#Начало форма для скрытых дверей
osobenosti = [('--','Особенности'),('внутреннее открывание','внутреннее открывание'),('с врезкой','с врезкой')]
metter_line = [('--','Материал кромки'),('алюминий.','алюминий'),('ABC','ABC')]
color_line = [('--','Цвет кромки'),('алюминий.','алюминий'),('под покраску.','под покраску'),('черный.','черный')]

class filter_skr(forms.Form):
    osoben = forms.TypedChoiceField(choices=osobenosti,coerce = str)
    metter = forms.TypedChoiceField(choices=metter_line,coerce = str)
    color = forms.TypedChoiceField(choices=color_line,coerce = str)
    price_scale_skr = forms.TypedChoiceField(choices=price_scale_choice,coerce = str)
#Конец формы для скрытых дверей