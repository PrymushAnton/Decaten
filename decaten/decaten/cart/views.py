from django.shortcuts import render
from catalog_product.models import *
from django.http import JsonResponse, HttpResponse
# Create your views here.

def cart(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
        session_key = request.session.session_key
        
    flavours = Flavour.objects.all()

    try:
        cart = Cart.objects.get(sessionkey=session_key)
    except:
        cart = Cart.objects.create(sessionkey=session_key)
        
    # print(cart.productincart_set.)
    prices = []
    count = 0
    for product in cart.productincart_set.all():
        product_obj = Product.objects.filter(id=product.product_id).values()
        product_obj = list(product_obj)
        # print(product.count)
        prices.append(int(product_obj[0]['price']) * product.count)
        count += product.count
        
    print(count)

  
    context = {
        "products": cart.productincart_set.all(),
        'flavours': flavours,
        'prices': prices,
        'count_cart': count,
    }
    
    return render(request, 'cart/cart.html', context)


def plus_count(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
        session_key = request.session.session_key
        
    try:
        cart = Cart.objects.get(sessionkey=session_key)
    except:
        cart = Cart.objects.create(sessionkey=session_key)
    
    try:
        hidden_input = request.POST.get('product_id')
        
        
        hidden_input = hidden_input.split(',')
        product_obj = Product.objects.filter(id=hidden_input[1]).values()
        price = list(product_obj)[0]['price']
        
        product = cart.productincart_set.get(product_id=hidden_input[1], flavour_id=hidden_input[0])

        
        product.count += 1
        count = product.count
        
        final_price = price * count
        product.save()
        
        count_cart = 0
        for product in cart.productincart_set.all():
            product_obj = Product.objects.filter(id=product.product_id).values()
            product_obj = list(product_obj)
            count_cart += product.count
        
        return JsonResponse({'count_cart':count_cart,'price': final_price,"count": count, 'product_id': hidden_input[1], 'flavour_id': hidden_input[0]})
    except:
        return HttpResponse()
    
    
    
def minus_count(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
        session_key = request.session.session_key
        
    try:
        cart = Cart.objects.get(sessionkey=session_key)
    except:
        cart = Cart.objects.create(sessionkey=session_key)
    
    
    try:
        hidden_input = request.POST.get('product_id')
        hidden_input = hidden_input.split(',')
        product_obj = Product.objects.filter(id=hidden_input[1]).values()
        price = list(product_obj)[0]['price']
        product = cart.productincart_set.get(product_id=hidden_input[1], flavour_id=hidden_input[0])
        if int(product.count) >= 1:
            product.count -= 1
            product.save()
        if int(product.count) < 1:
            product.delete()

        count = product.count
        final_price = price * count
        
        count_cart = 0
        for product in cart.productincart_set.all():
            product_obj = Product.objects.filter(id=product.product_id).values()
            product_obj = list(product_obj)
            count_cart += product.count
            
        return JsonResponse({'count_cart':count_cart,'price': final_price,"count": count, 'product_id': hidden_input[1], 'flavour_id': hidden_input[0]})
    except:
        return HttpResponse()
    


def delete_product(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
        session_key = request.session.session_key
        
    try:
        cart = Cart.objects.get(sessionkey=session_key)
    except:
        cart = Cart.objects.create(sessionkey=session_key)
    
    
    try:
        hidden_input = request.POST.get('product_id')
        hidden_input = hidden_input.split(',')
        product = cart.productincart_set.get(product_id=hidden_input[1], flavour_id=hidden_input[0])
        product.delete()
        products = list(cart.productincart_set.all().values())
        print(products)
        
        count = 0
        for product in cart.productincart_set.all():
            product_obj = Product.objects.filter(id=product.product_id).values()
            product_obj = list(product_obj)
            count += product.count
        print(count)
        
        return JsonResponse({'product_id': hidden_input[1], 'flavour_id': hidden_input[0], 'count_cart': count})
    except:
        return HttpResponse()



def error_empty(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
        session_key = request.session.session_key

    try:
        cart = Cart.objects.get(sessionkey=session_key)
    except:
        cart = Cart.objects.create(sessionkey=session_key)

    
    cart = list(cart.productincart_set.all().values())
    
    return JsonResponse({"products": cart})