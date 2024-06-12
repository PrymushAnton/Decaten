from django.shortcuts import render
from .models import *
from django.http import JsonResponse, HttpResponse



# Create your views here.
def catalog(request):
    names_of_filters = NameOfFilter.objects.all()
    print(names_of_filters)
    filter = None
    for name_of_filter in names_of_filters:
        name_of_filter = NameOfFilter.objects.get(name=name_of_filter)
        try:
            filter = Filter.objects.filter(name_of_filter = name_of_filter)
        except:
            continue
    
    all_products = Product.objects.all()
    
    amount_of_products = len(Product.objects.all())
    
    context = {
        'names_of_filters': names_of_filters,
        'list_of_filters': filter,
        'all_products': all_products,
        'amount_of_products': amount_of_products,
    }
    
    return render(request, 'catalog_product/catalog.html', context)


def filter_products(request):
    if request.method == 'POST':
        filters_true = request.POST.get('filters_true')
        filters_true = filters_true.split(',')
        
        products = []
        
        for filter_id in filters_true:
            product = Product.objects.filter(filters__id=filter_id).values()
            product = list(product)
            # print(product)
            products.append(product)
            # print(products)
        
        # products = list(products)
        # print(products)
        # ({'products':product})
        return JsonResponse({'products':products})
    else:
        return HttpResponse()

def filter_amount_of_products(request):
    amount_of_all_products = len(Product.objects.all())
    
    return JsonResponse()