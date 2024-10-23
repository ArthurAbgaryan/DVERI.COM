from django.shortcuts import render,get_object_or_404,redirect
from .models import products,categories,colors,properties,property_values,accessories
from cart.forms import CartForm
from .forms import SearchForm, measureForm
from django.contrib.postgres.search import SearchVector
from django.core.mail import send_mail
from django.conf import settings


def index(request,category = None,
          category_next = None,
          category_next_2 = None,):
    exclude_category_model_mezhkomnt = [332, 395, 193, 12, 394, 246]
    cart_form = CartForm()
    middle_c = []
    model_1 = []
    obj = products.objects.all()[:20]
    name_category_top = []
    if category:
        name_category_top = ['Главная']
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
                category_next_object = get_object_or_404(categories, id = category)
                name_category_top.append('/' + category_next_object.title + '/')
                model_c_id = []
                model_1 = categories.objects.filter(parent_id = category_next).exclude(id__in = exclude_category_model_mezhkomnt)
                if model_1:
                    for x in model_1:
                        model_c_id.append(x.id)
                    obj = products.objects.filter(category_id__in = model_c_id)
                else:
                    obj = products.objects.filter(category_id = category_next)
                if category_next_2:
                    category_next_2_object = get_object_or_404(categories, id = category_next)
                    name_category_top.append(category_next_2_object.title + '/')
                    obj = products.objects.filter(category_id = category_next_2)
        else:
            obj = products.objects.filter(category_id = category)
    return render(request,'doors/index.html',{'obj':obj,
                                              'cart_form':cart_form,
                                              'midle_cat':middle_c,
                                              'model_cat':model_1,
                                              'name_category_top':name_category_top})

def detail_card (request, pk, des=1, detail_color_id=None, detail_size = None):
    description_1 = des
    list_colors_id_this_obj = []
    category_2=[]
    name_category_top = ['Главная']
    category_1 =[]
    proper_dict = {}
    metal_acsessory = {}
    cart_form = CartForm()
    detail_obj = get_object_or_404(products,id = pk)
    detail_obj_category = categories.objects.get(id = detail_obj.category_id)
    if detail_obj_category.parent_id:
        category_1 = categories.objects.filter(parent_id = detail_obj_category.parent_id)
        category_2_parent = categories.objects.get(id = detail_obj_category.parent_id)

        if category_2_parent.parent_id:
            category_3_parent = categories.objects.get(id = category_2_parent.parent_id)
            name_category_top.append('/' + category_3_parent.title + '/' + category_2_parent.title + '/' + detail_obj_category.title)
        else:
            name_category_top.append('/' + category_2_parent.title + '/' + detail_obj_category.title)
        if category_2_parent.parent_id:
            category_2 = categories.objects.filter(parent_id = category_2_parent.parent_id)
        else:
            category_2 = category_1
    else:
        name_category_top.append('/' + detail_obj_category.title)
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
    if detail_obj.color_id:
        color_obj = colors.objects.get(id = detail_obj.color_id)
    else:
        color_obj =[]
    vendor_code = detail_obj.vendor_code
    if detail_size:
        for x in detail_obj.options:
            if x['title'] == detail_size:
                vendor_code = x['vendor_code']
    #Код описания товара
    if des == 1:
        for proper in detail_obj.properties:
            properti_1 = properties.objects.get(id = proper['id']).title
            properti_1_values = property_values.objects.get(id = proper['value_id']).title
            proper_dict[properti_1] = properti_1_values

    complectation = accessories.objects.filter(accessory_group_id = detail_obj.accessory_group_id)

    if des == 3:
        if detail_obj.accessory_properties:
            for m_a in detail_obj.accessory_properties:
                m_a_id = properties.objects.get(id = m_a['id']).title
                m_a_values = property_values.objects.get(id = m_a['value_id']).title
                metal_acsessory[m_a_id] = m_a_values
    context = {'detail_obj':detail_obj,
               'metal_acsessory':metal_acsessory,
               'complectation':complectation,
               'description_number':description_1,
               'proper_dict':proper_dict,
               'colors':detail_obj_colors,
               'color_obj':color_obj,
               'midle_cat': category_2,
               'model_cat': category_1,
               'vendor_code':vendor_code,
               'cart_form':cart_form,
               'name_category_top':name_category_top}

    return render(request, 'doors/detail_card.html',context)

def search(request):
    form_search = SearchForm()
    cart_form = CartForm()
    query = None
    results = []
    if 'query' in request.GET:
        form_search = SearchForm(request.GET)
    if form_search.is_valid():
        query = form_search.cleaned_data['query']
        results = products.objects.annotate(search = SearchVector('title','vendor_code')).filter(search = query)
    return render(request, 'doors/search_final.html',{'form_search':form_search,
                                                      'query': query,
                                                      'results':results,
                                                      'cart_form':cart_form})

def contacts(request):
    return render(request, 'doors/contacts.html')

def measure(request):
    if request.method == 'POST':
        form = measureForm(request.POST)
        form.save()
        send_mail("Замер",
                  "Вам отправил заявку на замер",
                  settings.EMAIL_HOST_USER,
                  ["abgaryanarthurelina@gmail.com"],
                  fail_silently=False,)
        return redirect ('doors:index')
    else:
        form = measureForm()
    return render(request, 'doors/measure.html', {'form':form})