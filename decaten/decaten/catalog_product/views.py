from django.shortcuts import render
from .models import *
from django.http import JsonResponse, HttpResponse
import json
import ast


# Create your views here.
def catalog(request):
    names_of_filters = NameOfFilter.objects.all()
    
    filters = []
    for name_of_filter in names_of_filters:
        # print(name_of_filter)
        name_of_filter = NameOfFilter.objects.get(name=name_of_filter)
        try:
            semi_filter = Filter.objects.filter(name_of_filter = name_of_filter)
            filters.append(semi_filter)
            
        except:
            continue
        
    all_products = Product.objects.all()
    
    products_values = Product.objects.all().values()
    products_values = list(products_values)
    prices = []
    
    for value in products_values:
        prices.append(int(value['price']))
        
    
    max_price = max(prices)
    min_price = min(prices)
    
    amount_of_products = len(Product.objects.all())

    all_flavours = Flavour.objects.all()
    
    context = {
        'names_of_filters': names_of_filters,
        'list_of_filters': filters,
        'all_products': all_products,
        'amount_of_products': amount_of_products,
        'all_flavours': all_flavours,
        'min_price': min_price,
        'max_price': max_price,
    }
    
    return render(request, 'catalog_product/catalog.html', context)


def filter_products(request):
    filters_true = request.POST.get('filters_true')
    
    
    filters_true = ast.literal_eval(filters_true)
    # print(filters_true)
    
    products_true = request.POST.get('filters_true')
    products_true = ast.literal_eval(products_true)
    for product_list in products_true:
        product_list.clear()

    # print('products_true: ',products_true)
    # print(products_true)
    # print(filters_true)
    
    filtered_products = []
    filters = []

    error = None


    max_price = request.POST.get('max_price')
    min_price = request.POST.get('min_price')
    all_products = Product.objects.all().values()
    filtered_products_by_price_ids = []
    for product in all_products:
        if int(product['price']) >= int(min_price) and int(product['price']) <= int(max_price):
            filtered_products_by_price_ids.append(int(product['id']))
    
    count = 0
    for filter_list in filters_true:
        product = Product.objects.filter(filters__in=filter_list)
        # print(product)
        # print(count)
        products_true[count].append(product)
        count += 1
    # print(products_true)
    
    
    def get_products(queryset):
        return list(queryset)
    
    # Перетворимо list_of_lists з QuerySet до списків з продуктами
    list_of_product_lists = [get_products(qs[0]) for qs in products_true if qs]

    # Фільтруємо порожні списки
    filtered_lists = [lst for lst in list_of_product_lists if lst]

    # Якщо є хоча б один непорожній список, знаходимо спільні елементи
    if filtered_lists:
        common_items = set(filtered_lists[0])
        for lst in filtered_lists[1:]:
            
            common_items.intersection_update(lst)
        # Перетворимо набір назад у список (якщо потрібно)
        common_items = list(common_items)
        print(common_items)
        if len(common_items) == 0:
            error = 1
    else:
        common_items = []

    # Перевірка результату
    # print(common_items)
    # count = 0
    # for item in common_items:
    #     print(type(item))
    #     common_items[count] = item
    #     count += 1
    values_list = [product.__dict__['id'] for product in common_items]
    # print(values_list)
    
    products = Product.objects.filter(id__in=values_list).values()
    products = list(products)
    # print(products)
    
    # products_true = [lst for lst in products_true if lst]
    
    
    # if products_true:
    #     common_items = set(products_true[0])
    #     for lst in products_true[1:]:
    #         common_items.intersection_update(lst)

    #     # Перетворимо набір назад у список (якщо потрібно)
    #     common_items = list(common_items)
    # else:
    #     common_items = []
    # print('common_items',common_items)
    
    
    
    
    
    
    
    # for product_list in products_true:
    #     if product_list:
    #         for product in product_list
    
    

    # filters_list = []
    # for filter in filters_true:
        # names_of_filters = Filter.objects.filter(id=filter)
    # products = Product.objects.filter(filters__id__in=filters_true)
        # filters_list.append(names_of_filters)
    # print(names_of_filters)
        
        
    # print(filters_list)
    # names_of_filters_list = []
    # for el in name_of_filters:
    #     print(el)
    #     name = NameOfFilter.objects.filter(id=el)
    #     print(name)
    #     names_of_filters_list.append(name)
        
    # print(names_of_filters_list)
        

    # name_of_filters = NameOfFilter.objects.all().values()
    # for filter in filters_true:
    #     # name_of_filters_ids.append(int(name['id']))
    #     print(filter)


    # try:
    #     filter = Filter.objects.filter(id__in=filters_true).values()
    #     for obj in filter:
    #         filters.append(obj['id'])
    #     filtered_products = Product.objects.filter(filters__id__in=filters).distinct().values()
    #     filtered_products = list(filtered_products)
        
    # except:
    #     pass
    # print(filters)
    # print(filtered_products)
    
    
    # 'products': products_true
    return JsonResponse({'products': products, 'error': error})





def get_flavour_image(request):
    value_of_selector = request.POST.get('value_of_selector')
    value_of_selector = value_of_selector.split(',')
    print(value_of_selector)
    flavour = Flavour.objects.filter(id=value_of_selector[0]).values()
    flavour = list(flavour)

    print(flavour)
    return JsonResponse({'flavour': flavour})



def product_image(request):
    
    flavours = Flavour.objects.all().values()
    flavours = list(flavours)
    
    return JsonResponse({"flavours":flavours})

def product_page(request, id):
    context = {'product': Product.objects.get(id=id)}
    context['flaur'] = Flavour.objects.filter(for_product = id)
    # filters = []
    # print(list(Product.objects.filter(id=id).filters.values()))
    # for obj in list(Product.objects.filter(id=id).values()):
    #     print(obj)
        # filters.append(obj['filters'])
        
    id_of_filters = []
    name_of_filters = []
    
    products = Product.objects.filter(id=id)
    
    product_filters = []
    
    list_of_names = []
    list_of_filters = []
    
    for product in products:
        product_filters_objs = list(product.filters.values('name_of_filter','name'))
        # filter = list(product.filters.values('name'))
        count = 0
        for product_obj in product_filters_objs:
            count += 1
            list_temp = []
            # for obj in product_obj:
            # id_of_filters.append(int(product_obj['name_of_filter']))
            # print(id_of_filters)
            name_of_filter = NameOfFilter.objects.filter(id=int(product_obj['name_of_filter'])).values('name')
            name_of_filter = list(name_of_filter)
            print(name_of_filter)
            
            filter = Filter.objects.filter(name=product_obj['name']).values('name')
            filter = list(filter)
            
            list_temp = [name_of_filter[0]['name']+':', filter[0]['name']]
            list_of_filters.append(list_temp)
            list_temp = []
        
    print(list_of_filters)
    context['list_of_filters'] = list_of_filters
    
    
   
    return render(request, 'catalog_product/product.html', context)


def add_to_cart(request):
    
    select = request.POST.get('selector')
    select = select.split(',')
    
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
        session_key = request.session.session_key

    # product_id = request.POST.get('id_product')
    
    try:
        cart = Cart.objects.get(sessionkey=session_key)
    except:
        cart = Cart.objects.create(sessionkey=session_key)        
    
    try:
        product = cart.productincart_set.get(product_id=select[1], flavour_id=select[0])
        product.count += 1
        product.save()
    except:
        product = cart.productincart_set.create(product_id=select[1], flavour_id=select[0], count=1)
    
    return HttpResponse(1)

