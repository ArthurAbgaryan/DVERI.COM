
from django.shortcuts import render,get_object_or_404
from .models import Order,OrderItem
from .forms import OrderForm
from cart.cart import Cart
from doors.models import products
from django.contrib.admin.views.decorators import staff_member_required
from django.template.loader import render_to_string,get_template
from django.http import HttpResponse,FileResponse
from django.conf import settings
import reportlab
import io
from reportlab.pdfgen import canvas
# from xhtml2pdf import pisa
"""
@staff_member_required
def admin_order_pdf(request, order_id):
    template = get_template('order/pdf.html')
    order = get_object_or_404(Order,id = order_id)
    html = template.render({'order':order})
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    return None


"""
@staff_member_required
def admin_order_pdf(request, order_id):
    buffer = io.BytesIO()
    order = get_object_or_404(Order, id = order_id)
    template = get_template('order/pdf.html')
    html = template.render({'order':order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Description'] = 'filename="order_{}"'.format(order.id)
    p = canvas.Canvas(response)
    p.drawString(100,100,html)
    p.showPage()
    p.save()
    return response


"""Вызывая библиотек weastprint мы передаем ей html в виде
строки и звписываем его как pdf в объект ответа response"""
"""
@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id = order_id)
    html = render_to_string('order/pdf.html',{'order':order}) #возврашает сгенерированные HTML в виде строки
    response = HttpResponse(content_type='application/pdf')
    response['Content-Desposition'] = 'filename="order_{}"'.format(order.id)
    weasyprint.HTML(string=html).write_pdf(response,stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
    return response
"""
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
