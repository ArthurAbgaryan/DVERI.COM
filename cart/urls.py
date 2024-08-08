from django.urls import path
from .views import cart_view,cart_add,cart_remove
app_name = 'cart'
urlpatterns = [
    path('cart_add/<int:product_id>/',cart_add, name = 'cart_add'),
    path('cart_view/',cart_view, name = 'cart_view')
]