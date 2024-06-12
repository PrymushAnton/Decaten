from django.shortcuts import render
from .models import Carusel
from catalog_product.models import Product

# Create your views here.
def main(request):
    context = {}
    images_for_carusel = Carusel.objects.all()
    all_products = Product.objects.all()
    context['images_for_carusel'] = images_for_carusel
    context['all_products'] = all_products
    return render(request, 'main/main.html', context)