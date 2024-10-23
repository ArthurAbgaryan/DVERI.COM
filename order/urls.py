from .views import order,admin_order,admin_order_pdf
from django.urls import path
app_name = 'order'

urlpatterns = [
    path('order/',order, name = 'order'),
    path('admin/order/<int:order_id>/',admin_order, name = 'admin_order'),
    path('admin/order/pdf/<int:order_id>/',admin_order_pdf, name='admin_pdf'),
]