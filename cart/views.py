import json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404,redirect
from .cart import Cart
from doors.models import products,accessories
from .forms import CartForm
from django.views.decorators.http import require_POST
from django.apps import apps
@require_POST
def cart_add(request, product_id,class_name):
    our_class = globals()[class_name]
    cart = Cart(request)
    object = get_object_or_404(our_class, id = product_id)
    form = CartForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product = object,
            quantity = cd['quantity'],
            update_quantity= cd['update'],
            class_name=class_name
            )
        cart.save()
        return redirect('doors:index')

@require_POST
def cart_add_ajax(request):
    print("--------------------------------------------------------------------------------------------------")
    data = json.loads(request.body)
    name_obj = str(data['nameClass'])
    model_name = apps.get_model('doors',name_obj)
    id_obj = int(data['id'])
    update = str(data['update'])
    if update == 'False':
        update = False
    else:
        update = True
    value = int(data['value'])
    objects = get_object_or_404(model_name,id = id_obj)
    print(objects)
    cart = Cart(request) #cart = Cart(request.POST)
    cart.add(
         product=objects,
         quantity=value,
         update_quantity=update,
         class_name = data['nameClass']
         )
    cart.save()
    print(cart.cart)
    return JsonResponse({'arthur':'arthur'})


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:cart_view')

def cart_remove(request, product_id):
    cart = Cart(request)
    object = get_object_or_404(products, id = product_id)
    cart.remove(object)

def cart_view(request):
    cart = Cart(request)
    for x in cart:
        print("x.product.title",x['product'].title)
    print("экранизация:",cart.cart)
    return render(request, 'cart/cart_list.html', {'cart_cart':cart.cart})

