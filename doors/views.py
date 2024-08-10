from django.shortcuts import render
from .models import products,categories
from cart.forms import CartForm

def index(request, category = None, category_next = None,category_next_2 = None):
    cart_form = CartForm()
    middle_c = []
    model_1 = []
    obj = products.objects.all()[:100]
    all_products = products.objects.all()
    all_categories_id = []
    for x in all_products:
        all_categories_id.append(x.category_id)
    all_category = categories.objects.filter(id__in=all_categories_id)
    main_categoies_list = []
    midle_categories = []
    model_categories = []
    for x in all_category:
        if x.parent_id:
            midle_cat = categories.objects.filter(id=x.parent_id)
            for y in midle_cat:
                if y.parent_id:
                    main_categoies_list.append(y.parent_id)
                    midle_categories.append(y.id)
                    model_categories.append(x.id)
                else:
                    main_categoies_list.append(y.id)
                    model_categories.append(x.id)
        else:
            main_categoies_list.append(x.id)
    main_category = categories.objects.filter(id__in =main_categoies_list ).exclude(id__in= [37,168])
    exclude_category_model_mezhkomnt = [332,395,193,12,394,246]

    if category:
        middle_c_id = []
        model_c_id = []
        middle_c = categories.objects.filter(parent_id = category).exclude(id__in= [270,590,238])
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



    return render(request,'doors/index.html',{'obj':obj,
                                              'cart_form':cart_form,
                                              'midle_cat':middle_c,
                                              'model_cat':model_1,
                                              'main_cat':main_category})

# def get_category(request):
#     all_products = products.objects.all()
#     all_categories_id = []
#     for x in all_products:
#         all_categories_id.append(x.category_id)
#     all_category = categories.objects.filter(id__in = all_categories_id)
#     main_categoies_list = []
#     midle_categories = []
#     model_categories = []
#     for x in all_category:
#         if x.parent_id:
#             midle_cat = categories.objects.filter(id = x.parent_id)
#             if midle_cat.parent_id:
#                 main_categoies_list.append(midle_cat.parent_id)
#                 midle_categories.append(midle_cat.id)
#                 model_categories.append(x.id)
#             else:
#                 main_categoies_list.append(midle_cat.id)
#                 model_categories.append(x.id)
#
#         else:
#             main_categoies_list.append(x.id)

# Create your views here.
