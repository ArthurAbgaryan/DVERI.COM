from .cart import Cart
from .forms import CartForm

def cart(request):
    cart = Cart(request)
    cart_f = CartForm()
    return {'cart':cart,'cart_f':cart_f}

# def cart_f(request):
#     cart_f = CartForm()
#     return {'cart_f':cart_f}