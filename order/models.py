from django.db import models
from doors.models import products,accessories
class Order(models.Model):
    first_name = models.CharField(max_length=250)
    e_mail = models.EmailField()
    address = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return "Order {}".format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE, related_name = 'items')
    product = models.ForeignKey(products,on_delete=models.CASCADE, related_name='order_item',null=True)
    accessorie = models.ForeignKey(accessories, on_delete=models.CASCADE, related_name='order_item1',null=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_cost(self):
        return self.price * self.quantity
    def __str__(self):
        return "{}".format(self.id)


# Create your models here.
