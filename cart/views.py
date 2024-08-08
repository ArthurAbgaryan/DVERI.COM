from django.shortcuts import render, get_object_or_404,redirect
from .cart import Cart
from doors.models import products
from .forms import CartForm
from django.views.decorators.http import require_POST

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    object = get_object_or_404(products, id = product_id)
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(
                product = object,
                quantity = cd['quantity'],
                update_quantity= cd['update']
            )
            cart.save()
            return redirect('doors:index')

def cart_remove(request, product_id):
    cart = Cart(request)
    object = get_object_or_404(products, id = product_id)
    cart.remove(object)

def cart_view(request):
    cart = Cart(request)
    return render(request, 'cart/cart_list.html', {'cart_cart':cart})


# Create your views here.
