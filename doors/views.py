from django.shortcuts import render,get_object_or_404
from .models import products,categories,colors
from cart.forms import CartForm



def index(request,category = None, category_next = None,category_next_2 = None):
    exclude_category_model_mezhkomnt = [332, 395, 193, 12, 394, 246]
    cart_form = CartForm()
    middle_c = []
    model_1 = []
    obj = products.objects.all()[:100]
    if category:
        middle_c_id = []
        model_c_id = []
        middle_c = categories.objects.filter(parent_id = category).exclude(id__in= [270,590,238])
        if middle_c:
            for m_c_id in middle_c:
                middle_c_id.append(m_c_id.id)
            model_category_list = categories.objects.filter(parent_id__in = middle_c_id).exclude(id__in = exclude_category_model_mezhkomnt)
            if model_category_list:
                for get_id_model in model_category_list:
                    model_c_id.append(get_id_model.id)
                obj = products.objects.filter(category_id__in = model_c_id)
            else:
                obj = products.objects.filter(category_id__in = middle_c_id)
            if category_next:
                model_c_id = []
                model_1 = categories.objects.filter(parent_id = category_next).exclude(id__in = exclude_category_model_mezhkomnt)
                if model_1:
                    for x in model_1:
                        model_c_id.append(x.id)
                    obj = products.objects.filter(category_id__in = model_c_id)
                else:
                    obj = products.objects.filter(category_id = category_next)
                if category_next_2:
                    obj = products.objects.filter(category_id = category_next_2)
        else:
            obj = products.objects.filter(category_id = category)
    return render(request,'doors/index.html',{'obj':obj,
                                              'cart_form':cart_form,
                                              'midle_cat':middle_c,
                                              'model_cat':model_1,})



def detail_card(request,pk,detail_color_id=None, detail_size = None):
    list_colors_id_this_obj = []
    category_2=[]
    category_1 =[]
    detail_obj = get_object_or_404(products,id = pk)
    detail_obj_category = categories.objects.get(id = detail_obj.category_id)
    if detail_obj_category.parent_id:
        category_1 = categories.objects.filter(parent_id = detail_obj_category.parent_id)
        category_2_parent = categories.objects.get(id = detail_obj_category.parent_id)

        if category_2_parent.parent_id:
            category_2 = categories.objects.filter(parent_id = category_2_parent.parent_id)
        else:
            category_2 = category_1


    if detail_color_id:
         detail_obj = get_object_or_404(products,title = detail_obj.title,
                                        category_id = detail_obj.category_id,
                                        glass_id=detail_obj.glass_id,
                                        color_id = detail_color_id)
    list_obj_with_name = products.objects.filter(title = detail_obj.title,
                                                 category_id = detail_obj.category_id,
                                                 glass_id = detail_obj.glass_id,
                                                 )
    for x in list_obj_with_name:
        list_colors_id_this_obj.append(x.color_id)
    detail_obj_colors = colors.objects.filter(id__in = list_colors_id_this_obj)
    color_obj = colors.objects.get(id = detail_obj.color_id)
    vendor_code = detail_obj.vendor_code
    if detail_size:
        for x in detail_obj.options:
            if x['title'] == detail_size:
                vendor_code = x['vendor_code']


    return render(request, 'doors/detail_card.html',{'detail_obj':detail_obj,
                                                     'colors':detail_obj_colors,
                                                     'color_obj':color_obj,
                                                     'midle_cat': category_2,
                                                     'model_cat': category_1,
                                                     'vendor_code':vendor_code,
                                                     })

