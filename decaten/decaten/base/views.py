from django.shortcuts import render
from catalog_product.models import *
from django.http import JsonResponse

# Create your views here.
def base(request):
    
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
        
    print(count)
    context = {
        'count_cart': count,
    }
    
    return render(request, 'base/base.html', context)

def count_cart(request):
    print(123123123123123)
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
        
    # print(count)
    # context = {
    #     'count_cart': count,
    # }
    print(count)
    return JsonResponse({'count_cart':count})
    