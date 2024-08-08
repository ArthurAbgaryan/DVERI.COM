from django.contrib import admin
from .forms import categories_forms
from .models import categories,colors,color_groups,glasses,accessory_groups,accessories,properties,property_values,attributes,attributeValues,trademarks,products
from django.urls import path
import json
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import reverse,render
@admin.register(glasses)
class glasses_admin(admin.ModelAdmin):
    list_display = ['title']
@admin.register(accessory_groups)
class accessory_groups_admin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(accessories)
class accessories_admin(admin.ModelAdmin):
    list_display = ['accessory_group_id','title','pictures','quantity','price','price_dealer','discount','discount_dealer','label','vendor_code','is_telescopic']

@admin.register(properties)
class properties_admin(admin.ModelAdmin):
    list_display = ['title','is_accessory','position']

@admin.register(property_values)
class property_values_admin(admin.ModelAdmin):
    list_display = ['property_id','product_id','title']

@admin.register(attributes)
class attributes_admin(admin.ModelAdmin):
    list_display = ['position','title']


@admin.register(attributeValues)
class attributeValues_admin(admin.ModelAdmin):
    list_display = ['attribute_id','title','is_generation_hidden','generation_title','description','position']

@admin.register(trademarks)
class trademarks_admin(admin.ModelAdmin):
    list_display = ['url','title']


@admin.register(products)
class product_admin(admin.ModelAdmin):
    list_display = ['title','url','category_id','accessory_group_id','color_id','glass_id','trademark_id','price','price_dealer','discount','discount_dealer','label','vendor_code','position','pictures','options','properties','accessory_properties','analogs','related_products']


@admin.register(categories)
class categories_admin(admin.ModelAdmin):
    list_display = ['id','title','parent_id','lft','rgt']

    def get_urls(self):
        url = super().get_urls()
        url.insert(-1,path('json_load/',self.json_load))
        return url

    def json_load(self,request):
        if request.method == "POST" and request.FILES['json_file']:
            form = categories_forms(request.POST,request.FILES)
            if form.is_valid():
                form_object = form.save()
                with form_object.json_file.open('r') as json_files:
                    data_json = json.load(json_files)
                    data_keys = data_json.keys()
                    for key in data_keys:
                        work_main = globals()[key]
                        if work_main.objects.all() !=[]:
                            work_main.objects.all().delete()
                        work_main.objects.bulk_create([work_main(**row) for row in data_json[key]])
                    messages.success(request, 'файл успешно загружен')
                    return HttpResponseRedirect(reverse('admin:index'))
        else:
            form = categories_forms()
        return render(request, 'admin/json_import.html',{'form':form})

@admin.register(colors)
class color_admin(admin.ModelAdmin):
    list_display = ['id','title','color_group_id','picture','position']

@admin.register(color_groups)
class color_admin(admin.ModelAdmin):
    list_display = ['id','title','position']

# Register your models here.
