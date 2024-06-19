from django.shortcuts import render
from .models import *
from django.http import JsonResponse, HttpResponse



# Create your views here.
def catalog(request):
    names_of_filters = NameOfFilter.objects.all()
    
    filters = []
    for name_of_filter in names_of_filters:
        print(name_of_filter)
        name_of_filter = NameOfFilter.objects.get(name=name_of_filter)
        try:
            semi_filter = Filter.objects.filter(name_of_filter = name_of_filter)
            filters.append(semi_filter)
            
        except:
            continue
        
    
    # for name_of_semifilter in filters:
    #     for name_of_filtersemi in name_of_semifilter:
    #         print(name_of_filtersemi.name_of_filter)
    
    all_products = Product.objects.all()
    
    amount_of_products = len(Product.objects.all())

    all_flavours = Flavour.objects.all()
    
    context = {
        'names_of_filters': names_of_filters,
        'list_of_filters': filters,
        'all_products': all_products,
        'amount_of_products': amount_of_products,
        'all_flavours': all_flavours,
    }
    
    return render(request, 'catalog_product/catalog.html', context)


def filter_products(request):
    filters_true = request.POST.get('filters_true')
    filters_true = filters_true.split(',')
    # filters_true = [ int(filter_true) for filter_true in filters_true ]
    
    filtered_products = []
    filters = []

    try:
        
        filter = Filter.objects.filter(id__in=filters_true).values()
        for obj in filter:
            filters.append(obj['id'])
        filtered_products = Product.objects.filter(filters__id__in=filters).distinct().values()
        filtered_products = list(filtered_products)
        
    except:
        pass
    print(filters)
    print(filtered_products)

    # filtered_products = Product.objects.all()
    # for filter_id in filters:
    #     filtered_products = filtered_products.filter(filters__id=filter_id).values()
    
    
    

    
    # try:
    # for filter in filters:
    # count = 0
    # products = [count += 1, Product.objects.filter(filters__id=filters[filter_obj['id']]) for filter_obj in filter]   
    # for filter_obj in filter:
    #     count += 1
    #     print(count)
    #     product = Product.objects.filter(filters__id=filters[count])
    #     print(product)
        # products.append(product)
    # product = Product.objects.filter(filters__in=filters)
    # product = Product.objects.all()
    # product = list(product)
    # print(products)
    # for prod in product:
    #     print(prod.name)
        # products.append(product)
    # except:
    #     pass
    # print(product)
    # for obj in product_obj:
        
    #     flavour = Flavour.objects.filter(for_product=obj).values()
    #     flavour = list(flavour)
    #     flavours.append(flavour)

    # 'products':products
    return JsonResponse({'products': filtered_products})





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
    
    
    # context['filters'] = product_filters
    
    # for product in product_filters:
    #     for obj in product:
    #         id_of_filters.append(int(obj['name_of_filter']))
    
    # for id in id_of_filters:
    #     name_of_filters.append(list(NameOfFilter.objects.filter(id=id).values('name')))

    # context['name_of_filters'] = name_of_filters
    
    # print(name_of_filters)
    # print(product_filters)
    
    # for list_of_names_obj in name_of_filters:
    #     list_of_names.append(list_of_names_obj)
    #     breakpoint
        
    # for list_of_filters_obj in product_filters:
    #     list_of_filters.append(list_of_filters_obj)
    #     break
        
    # print(list_of_names)
    # print(list_of_filters)
    # for product in product_filters:
    #     for obj in product:
    #         print(obj)
    # print(product_filters)
    # for product in product_filters:
    #     count = 0
    #     for filter in name_of_filters:
    #         count_new = 0
    #         for obj in product:
    #             if count_new == 1:
    #                 break
    #             else:
    #                 for obj_filter in filter:
    #                     if count == 1:
    #                         break
    #                     else:
    #                         list_of_filters.append([obj_filter['name'], obj['name']])
    #                         count += 1
    #                         count_new += 1
    
    # print(list_of_filters)
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