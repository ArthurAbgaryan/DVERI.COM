from django.shortcuts import render,get_object_or_404
from .models import Order,OrderItem
from .forms import OrderForm
from cart.cart import Cart
from doors.models import products
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_order(request, order_id):
    order = get_object_or_404(Order, id = order_id)
    return render(request, 'admin/orders/order/admin_detail.html', {'order':order})

def order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                if item['product'].__class__ == products:
                    OrderItem.objects.create(order = order,
                                            product = item['product'],
                                            quantity = item['quantity'],
                                            price = item['price'])
                else:
                    OrderItem.objects.create(order=order,
                                             accessorie=item['product'],
                                             quantity=item['quantity'],
                                             price=item['price'])
            return render(request, 'order/order-finish.html',{'order':order})

    else:
        form = OrderForm()
    return render(request, 'order/order.html', {'form':form,'cart':cart})

# Create your views here.
