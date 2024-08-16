from .models import categories,products

def category(request):
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
    return {'main_cat':main_category}
