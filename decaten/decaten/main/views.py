from django.shortcuts import render
from .models import Carusel
from catalog_product.models import Product, Flavour
from django.http import JsonResponse

# Create your views here.
def main(request):
    context = {}
    images_for_carusel = Carusel.objects.all()
    all_products = Product.objects.all()
    print(all_products)
    products = []
    count = 0
    for product in all_products:
        count += 1
        if count <= 4:
            products.append(product)
    print(products)
    
    context['images_for_carusel'] = images_for_carusel
    context['products'] = products
    context['all_flavours'] = Flavour.objects.all()
    return render(request, 'main/main.html', context)

def product_flavour_main(request):
    
    value_of_selector = request.GET.get('value_of_selector')
    value_of_selector = value_of_selector.split(',')
    
    flavour = Flavour.objects.filter(id=value_of_selector[0]).values()
    flavour = list(flavour)

    print(flavour)

    return JsonResponse({'flavour': flavour})


def product_image_main(request):
        
    flavours = Flavour.objects.all().values()
    flavours = list(flavours)
    
    return JsonResponse({"flavours":flavours})