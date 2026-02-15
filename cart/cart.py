import requests
from django.conf import settings
from doors.models import products,accessories
from decimal import Decimal


class Cart(object):
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID]={}
        self.cart = cart

    # def add(self,product,quantity=1,update_quantity = False):
    #     product_id = str(product.id)
    #     if product_id not in self.cart:
    #         self.cart[product_id] = {'quantity':0, 'price':str(product.price)}
    #     if update_quantity:
    #         self.cart[product_id]['quantity'] = quantity
    #     else:
    #         self.cart[product_id]['quantity'] += quantity
    #     self.save()
    def add(self,product,class_name,quantity=1,update_quantity = False):
        product_id = str(product.id)
        str_class_name = str(class_name)
        if str_class_name not in self.cart:
            self.cart[str_class_name] ={}
        if product_id not in self.cart[str_class_name]:
            self.cart[class_name][product_id] = {'quantity':0, 'price':str(product.price)}
        if update_quantity:
            self.cart[class_name][product_id]['quantity'] = quantity
        else:
            self.cart[class_name][product_id]['quantity'] += quantity
        self.save()

        #print("Содержимое cart: ", self.cart['accessories']) #Экранизация
        #print("Длинна cart accessories: ", len(self.cart['accessories']))#экранизация
        print("Длинна cart all : ", len(self.cart))  # экранизация
    '''Помечаем сессию как измененной'''
    def save(self):
        self.session.modified = True
    def remove(self,product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.cart

    def __iter__(self):
        #products_id = self.cart.keys()
        class_keys = self.cart.keys()
        for x in class_keys:
            name = str(x)
            className = globals()[name]
            id_list = self.cart[name].keys()
            class_keys_id = className.objects.filter(id__in =id_list )
            cart = self.cart.copy()
            for product in class_keys_id:
                cart[name][str(product.id)]['product'] = product

            if cart:
                for item in cart[name].values():
                    item['price'] = Decimal(item['price'])
                    item['total_price'] = item['quantity'] * item['price']
                    yield item

    # def __iter__(self):
    #     products_id = self.cart.keys()
    #     products_s_1 = accessories.objects.filter(id__in = products_id)
    #     products_s = products.objects.filter(id__in = products_id)
    #     cart = self.cart.copy()
    #     for product in products_s:
    #         cart[str(product.id)]['product'] = product
    #     for product_1 in products_s_1:
    #         cart[str(product_1.id)]['product1'] = product_1
    #     if cart:
    #         for item in cart.values():
    #             item['price'] = Decimal(item['price'])
    #             item['total_price'] = item['quantity'] * item['price']
    #             yield item
#--------------------------------------------------------------------------------------
        # for product_1 in products_s_1:
        #     cart[str(product_1.id)]['product'] = product_1
        #     if cart:
        #         for item in cart.values():
        #             item['price'] = Decimal(item['price'])
        #             item['total_price'] = item['quantity'] * item['price']
        #             yield item

    def __len__(self):
        return (sum(item['quantity'] for item in self.cart['products'].values())+
               sum(item1['quantity'] for item1 in self.cart['accessories'].values()))

    def get_total_price(self):
        return (sum(Decimal(item['price'])*item['quantity'] for item in self.cart['products'].values())+
                sum(Decimal(item1['price'])*item1['quantity'] for item1 in self.cart['accessories'].values()))

    def clear(self):
        del self.session[settings.CART_SESSION_ID]