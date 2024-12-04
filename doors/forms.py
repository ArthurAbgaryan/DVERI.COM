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
price_scale_choice = [('--','По умолчанию'),('Сначала дешевле','Сначала дешевле'),('Сначала дороже','Сначала дороже')]
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

#Начало форма для специальных дверей
type_spc = [('--','Тип'),('остекленные','остекленные'),('глухие','глухие')]
color_spc = [('--','Цвет'),('белый','белый'),('светлый','светлый'),('темный','темный')]

class filter_spec(forms.Form):
    type_c = forms.TypedChoiceField(choices=type_spc,coerce = str)
    color_c = forms.TypedChoiceField(choices=color_spc,coerce = str)
    price_scale_spc = forms.TypedChoiceField(choices=price_scale_choice,coerce = str)
#Конец формы для специальных дверей


#Начало форма для арок и порталов
view_arki = [('--','Вид'),('арки','арки'),('порталы','порталы')]
osobenosti_ark = [('--','Особенности'),('painted wood','painted wood')]
style_ark = [('--','Стиль'),('классика','классика'),('модерн','модерн')]
color_arki = [('--','Цвет'),('темный','темный'),('белый','белый'),('светлый','светлый'),('черный','черный')]

class filter_arki_and_portal(forms.Form):
    vid = forms.TypedChoiceField(choices=view_arki,coerce = str)
    style = forms.TypedChoiceField(choices=style_ark,coerce = str)
    osobenosti_arki = forms.TypedChoiceField(choices=osobenosti_ark,coerce = str)
    color_arki = forms.TypedChoiceField(choices=color_arki,coerce = str)
    price_scale_ark = forms.TypedChoiceField(choices=price_scale_choice,coerce = str)
#Конец формы для арок и порталов


#Начало форма для плинтусов
status_plintus = [('--','Статус'),('sale','sale'),('скоро','скоро'),('складская программа','складская программа')]
color_plintus = [('--','Цвет'),('белый','белый'),('светлый','светлый'),('темный','темный'),('хром','хром'),('под покраску','под покраску')]

class filter_plintus(forms.Form):
    color_pl = forms.TypedChoiceField(choices=color_plintus,coerce = str)
    status_pl = forms.TypedChoiceField(choices=status_plintus,coerce = str)
    price_scale_plintus = forms.TypedChoiceField(choices=price_scale_choice,coerce = str)
#Конец формы для плинтусов


#Начало форма для деко реек
status_deko = [('--','Статус'),('складская программа','складская программа')]
color_deko = [('--','Цвет'),('белый','белый'),('светлый','светлый'),('темный','темный'),('черный','черный'),('под покраску','под покраску')]

class filter_deko(forms.Form):
    color_dk = forms.TypedChoiceField(choices=color_deko,coerce = str)
    status_dk = forms.TypedChoiceField(choices=status_deko,coerce = str)
    price_scale_dk = forms.TypedChoiceField(choices=price_scale_choice,coerce = str)
#Конец формы для деко реек



#Начало форма для фурнитура
status_furnitura = [('--','Статус'),('sale','sale'),('hit','хит'),('складская программа','складская программа')]
color_furnitura = [('--','Цвет'),('хром','хром'),('золото','золото'),('бронза','бронза'),('серебро','серебро'),('серый','серый'),('коричневый','коричневый'),('белый','белый'),('светлый','светлый'),('темный','темный'),('черный','черный')]

class filter_furnitura(forms.Form):
    color_fr = forms.TypedChoiceField(choices=color_furnitura,coerce = str)
    status_fr = forms.TypedChoiceField(choices=status_furnitura,coerce = str)
    price_scale_fr = forms.TypedChoiceField(choices=price_scale_choice,coerce = str)
#Конец формы для фурнитура

#Начало форма для фурнитура
status_montazh = [('--','Статус'),('sale','sale'),('hit','хит'),('складская программа','складская программа')]
color_montazh = [('--','Цвет'),('светлый','светлый'),('черный','черный')]

class filter_montazh(forms.Form):
    color_mzh = forms.TypedChoiceField(choices=color_montazh,coerce = str)
    status_mzh = forms.TypedChoiceField(choices=status_montazh,coerce = str)
    price_scale_mzh = forms.TypedChoiceField(choices=price_scale_choice,coerce = str)
#Конец формы для фурнитура