import requests
from django.conf import settings
from doors.models import products
from decimal import Decimal


class Cart(object):
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID]={}
        self.cart = cart

    def add(self,product,quantity=1,update_quantity = False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0,'price':str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] == quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save

    '''Помечаем сессию как измененной'''
    def save(self):
        self.session.modified = True

    def remove(self,product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.cart

    def __iter__(self):
        products_id = self.cart.keys()
        products_s = products.objects.filter(id__in = products_id)
        cart = self.cart.copy()
        for product in products_s:
            cart[str(product.id)]['product'] = product
        if cart:
            for item in cart.values():
                item['price'] = Decimal(item['price'])
                item['total_price'] = item['quantity'] * item['price']
                yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price'])*item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]