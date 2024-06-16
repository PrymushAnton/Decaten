from django.shortcuts import render
from .models import *
from django.http import JsonResponse, HttpResponse



# Create your views here.
def catalog(request):
    names_of_filters = NameOfFilter.objects.all()
    filter = None
    for name_of_filter in names_of_filters:
        name_of_filter = NameOfFilter.objects.get(name=name_of_filter)
        try:
            filter = Filter.objects.filter(name_of_filter = name_of_filter)
        except:
            continue
    
    all_products = Product.objects.all()
    
    amount_of_products = len(Product.objects.all())

    all_flavours = Flavour.objects.all()
    
    context = {
        'names_of_filters': names_of_filters,
        'list_of_filters': filter,
        'all_products': all_products,
        'amount_of_products': amount_of_products,
        'all_flavours': all_flavours,
    }
    
    return render(request, 'catalog_product/catalog.html', context)


def filter_products(request):
    filters_true = request.POST.get('filters_true')
    filters_true = filters_true.split(',')
    
    products = []
    
    # all_products = Product.objects.all()
    # flavours = []
    
    for filter_id in filters_true:
        product = Product.objects.filter(filters__id=filter_id).values()
        product = list(product)
        # print(product)
        products.append(product)
    #     for obj in product_obj:
            
    #         flavour = Flavour.objects.filter(for_product=obj).values()
    #         flavour = list(flavour)
    #         flavours.append(flavour)

    print(products)

    return JsonResponse({'products':products})





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

    
    if request.method == 'POST':
        select = request.POST.get('selector')
        select = select.split(',')
        print(select)
        
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

    
    return render(request, 'catalog_product/product.html', context)