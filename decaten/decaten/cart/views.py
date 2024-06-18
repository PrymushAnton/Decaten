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
              
    context = {
        "products": cart.productincart_set.all(),
        'flavours': flavours,
    }
    # print(cart.productincart_set.all().values())
    
    # if request.method == "POST":
        
        # if request.POST.get('minus'):
        #     try:
        #         hidden_input = request.POST.get('minus')
        #         hidden_input = hidden_input.split(',')
        #         product = cart.productincart_set.get(product_id=hidden_input[1], flavour_id=hidden_input[0])
        #         if product.count > 0:
        #             product.count -= 1
        #         if product.count <= 0:
        #             product.delete()
        #         product.save()
        #     except:
        #         pass
        # if request.POST.get('plus'):
        #     try:
        #         hidden_input = request.POST.get('plus')
        #         hidden_input = hidden_input.split(',')
        #         product = cart.productincart_set.get(product_id=hidden_input[1], flavour_id=hidden_input[0])
        #         product.count += 1
        #         product.save()
        #     except:
        #         pass
        # if request.POST.get('delete'):
        #     try:
        #         hidden_input = request.POST.get('delete')
        #         hidden_input = hidden_input.split(',')
        #         print(hidden_input)
        #         product = cart.productincart_set.get(product_id=hidden_input[1], flavour_id=hidden_input[0])
        #         product.delete()
        #     except:
        #         pass
    
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
        product = cart.productincart_set.get(product_id=hidden_input[1], flavour_id=hidden_input[0])
        product.count += 1
        count = product.count
        product.save()
        
        return JsonResponse({"count": count, 'product_id': hidden_input[1]})
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
        product = cart.productincart_set.get(product_id=hidden_input[1], flavour_id=hidden_input[0])
        if int(product.count) >= 1:
            product.count -= 1
            product.save()
        if int(product.count) < 1:
            product.delete()

        count = product.count
        return JsonResponse({"count": count, 'product_id': hidden_input[1]})
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
        return JsonResponse({'product_id': hidden_input[1]})
    except:
        return HttpResponse()
