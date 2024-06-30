from django.shortcuts import render
from catalog_product.models import *
from django.http import JsonResponse
from cart.models import *
import requests, re

# Create your views here.
# def base(request):
    
#     session_key = request.session.session_key
#     if not session_key:
#         request.session.cycle_key()
#         session_key = request.session.session_key
        
#     try:
#         cart = Cart.objects.get(sessionkey=session_key)
#     except:
#         cart = Cart.objects.create(sessionkey=session_key)

#     count = 0
#     for product in cart.productincart_set.all():
#         product_obj = Product.objects.filter(id=product.product_id).values()
#         product_obj = list(product_obj)
#         count += product.count
        
#     print(count)
#     context = {
#         'count_cart': count,
        
#     }
    
#     return render(request, 'base/base.html', context)

# def count_cart(request):
#     # print(123123123123123)
#     session_key = request.session.session_key
#     if not session_key:
#         request.session.cycle_key()
#         session_key = request.session.session_key
        
#     try:
#         cart = Cart.objects.get(sessionkey=session_key)
#     except:
#         cart = Cart.objects.create(sessionkey=session_key)

#     count = 0
#     for product in cart.productincart_set.all():
#         product_obj = Product.objects.filter(id=product.product_id).values()
#         product_obj = list(product_obj)
#         count += product.count
        
#     # print(count)
#     # context = {
#     #     'count_cart': count,
#     # }
#     # print(count)
#     return JsonResponse({'count_cart':count})
    

def code_data(data):
    new_data = {}
    for message in data:
        index_of_message = data.index(message)
        for i in message:
            new_data[f"{i}{index_of_message}"] = [message[i]]
    return new_data

def decode_from_query_dict(data):
    role = ""
    new_messages = []
    for key in data:
        if re.search("role", key):
            role = data[key]
        elif re.search("content", key):
            new_messages.append({"role" : role, "content" : data[key]})
    return new_messages

def support_chat(request):
    if request.method == "POST":
        messages = request.POST
        print(messages)
        messages = decode_from_query_dict(messages)
        url = 'https://yaroslavsamchukapi.onrender.com/post/'
        
        messages = code_data(messages)
        response = requests.post(url, data=messages)

        print(response.status_code)
        print(response.json())
        return JsonResponse(data=response.json())

    return render(request, "base/support.html")