from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Order, OrderItem
from django.urls import reverse

class OrderItemTabular(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product','accessorie']

def admin_detail_mark(obj):
    return mark_safe('<a href="{}">Detail</a>'.format(reverse('order:admin_order',args=[obj.id])))

@admin.register(Order)
class OderAdmin(admin.ModelAdmin):
    list_display = ['first_name','e_mail','address','created','update','paid',admin_detail_mark]
    list_filter = ['created','update','paid']
    inlines = [OrderItemTabular]
# Register your models here.
