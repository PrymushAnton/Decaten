from django.shortcuts import render
from .models import *
from django.http import JsonResponse, HttpResponse
import json
import ast
from cart.models import *


# Create your views here.
def catalog(request):
    names_of_filters = NameOfFilter.objects.all()
    
    filters = []
    for name_of_filter in names_of_filters:
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
    
    
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
        session_key = request.session.session_key
        
    try:
        cart = Cart.objects.get(sessionkey=session_key)
    except:
        cart = Cart.objects.create(sessionkey=session_key)

    count = 0
    for product in cart.productincart_set.all():
        product_obj = Product.objects.filter(id=product.product_id).values()
        product_obj = list(product_obj)
        count += product.count
    
    context = {
        'names_of_filters': names_of_filters,
        'list_of_filters': filters,
        'all_products': all_products,
        'amount_of_products': amount_of_products,
        'all_flavours': all_flavours,
        'min_price': min_price,
        'max_price': max_price,
        'count_cart': count,
    }
    
    return render(request, 'catalog_product/catalog.html', context)


def filter_products(request):
    filters_true = request.POST.get('filters_true')
    
    
    
    filters_true = ast.literal_eval(filters_true)
    print(filters_true)
    
    products_true = request.POST.get('filters_true')
    products_true = ast.literal_eval(products_true)
    for product_list in products_true:
        product_list.clear()

    error = None


    max_price = request.POST.get('max_price')
    min_price = request.POST.get('min_price')
    all_products = Product.objects.all().values()

    filtered_products_by_price_ids = []
    for product in all_products:
        if int(product['price']) >= int(min_price) and int(product['price']) <= int(max_price):
            filtered_products_by_price_ids.append(int(product['id']))
        

    products_price = Product.objects.filter(id__in=filtered_products_by_price_ids)


    count = 0
    for filter_list in filters_true:
        product = Product.objects.filter(filters__in=filter_list)
        # print(product)
        # print(count)
        products_true[count].append(product)
        count += 1
    
    # products_true
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
        if len(common_items) == 0:
            error = 1
    else:
        common_items = []
    values_list = [product.__dict__['id'] for product in common_items]
    products = Product.objects.filter(id__in=values_list)

    
    if len(list(products.values())) != 0 and len(list(products_price.values())) != 0:
        common_products_price = products.intersection(products_price)
        if len(list(common_products_price)) == 0:
            error = 1
        products = list(common_products_price.values())
    elif len(list(products_price.values())) == 0 and len(list(products.values())) == 0:
        error = 1
        products = list(products_price.values())
    elif len(list(products.values())) == 0:
        if len(list(products_price.values())) != 0 and error != 1:
            products = list(products_price.values())
        else:
            products = list(products.values())
    else:
        error = 1

    return JsonResponse({'products': products, 'error': error})





def get_flavour_image(request):
    value_of_selector = request.POST.get('value_of_selector')
    value_of_selector = value_of_selector.split(',')
    # print(value_of_selector)
    flavour = Flavour.objects.filter(id=value_of_selector[0]).values()
    flavour = list(flavour)

    # print(flavour)
    return JsonResponse({'flavour': flavour})



def product_image(request):
    
    flavours = Flavour.objects.all().values()
    flavours = list(flavours)
    
    return JsonResponse({"flavours":flavours})

def product_page(request, id):
    context = {}
    try:
        context = {'product': Product.objects.get(id=id)}
    
        context['flaur'] = Flavour.objects.filter(for_product = id)

        session_key = request.session.session_key
        if not session_key:
            request.session.cycle_key()
            session_key = request.session.session_key
            
        try:
            cart = Cart.objects.get(sessionkey=session_key)
        except:
            cart = Cart.objects.create(sessionkey=session_key)

        count = 0
        for product in cart.productincart_set.all():
            product_obj = Product.objects.filter(id=product.product_id).values()
            product_obj = list(product_obj)
            count += product.count
            
        context['count_cart'] = count

            
        # id_of_filters = []
        # name_of_filters = []
        
        products = Product.objects.filter(id=id)
        # product_filters = []
        
        # list_of_names = []
        list_of_filters = []
        
        for product in products:
            product_filters_objs = list(product.filters.values('name_of_filter','name'))

            # filter = list(product.filters.values('name'))
            count = 0
            for product_obj in product_filters_objs:
                count += 1
                list_temp = []

                name_of_filter = NameOfFilter.objects.filter(id=int(product_obj['name_of_filter'])).values('name')
                name_of_filter = list(name_of_filter)
                
                filter = Filter.objects.filter(name=product_obj['name']).values('name')
                filter = list(filter)
                list_temp = [name_of_filter[0]['name']+':', filter[0]['name']]
                print(list_temp)
                list_of_filters.append(list_temp)
                list_temp = []
            
        context['list_of_filters'] = list_of_filters
    except:
        pass
    
   
    return render(request, 'catalog_product/product.html', context)


def add_to_cart(request):
    select = request.POST.get('selector')
    select = select.split(',')
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
        session_key = request.session.session_key
    
    try:
        cart = Cart.objects.get(sessionkey=session_key)
    except:
        cart = Cart.objects.create(sessionkey=session_key)
        
          
    flavour = Flavour.objects.filter(id=select[0]).values()
    flavour = list(flavour)
    
    try:
        product = cart.productincart_set.get(product_id=select[1], flavour_id=select[0])
        if flavour[0]['count_of_product'] > product.count:
            
            product.count += 1
            product.save()
        else:
            pass
    except:
        if flavour[0]['count_of_product'] > 0:
            product = cart.productincart_set.create(product_id=select[1], flavour_id=select[0], count=1)
        else:
            pass
    
    count_cart = 0
    for product in cart.productincart_set.all():
        product_obj = Product.objects.filter(id=product.product_id).values()
        product_obj = list(product_obj)
        count_cart += product.count
        
    
    return JsonResponse({'count_cart':count_cart})

