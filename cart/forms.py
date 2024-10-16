from django import forms

PRODUCT_QUANTITY_CHOICE = [(i,str(i)) for i in range(1,21)]

class CartForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICE,coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)