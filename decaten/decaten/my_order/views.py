from django.shortcuts import render, redirect
import requests
from django.http import JsonResponse, HttpResponse
from .models import *
from catalog_product.models import *
from django.contrib.auth import authenticate

API_KEY = 'a82d9d12e5f74a8692792b6930d55bc4'
BASE_URL = 'https://api.novaposhta.ua/v2.0/json/'


def my_order(request):
    
    # cities = get_cities()
    # print(cities)
    # print(request.user.password)
    # user = authenticate(username=request.user.username, password=request.user.password)
    # print(user)
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
        session_key = request.session.session_key
        
    try:
        cart = Cart.objects.get(sessionkey=session_key)
    except:
        cart = Cart.objects.create(sessionkey=session_key)
    
    price_of_order = 0
    products = []
    try:
        products_in_cart = cart.productincart_set.all().values()
        products_in_cart = list(products_in_cart)
        print(products_in_cart)
        for product in products_in_cart:
            # print(product['id'])
            product_obj = Product.objects.filter(id=product['product_id']).values()
            product_obj = list(product_obj)
            # print(product_obj[0]['price'])
            price_of_order += int(product_obj[0]['price']) * int(product['count'])
    except:
        pass
        
        
    
    context = {'price':price_of_order}
    
    return render(request, 'my_order/my_order.html', context)


def get_areas():
    data = {
        "apiKey": API_KEY,
        "modelName": "Address",
        "calledMethod": "getAreas",
        "methodProperties": {}
    }
    response = requests.post(BASE_URL, json=data)
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        return []

def get_cities(area_ref):
    data = {
        "apiKey": API_KEY,
        "modelName": "Address",
        "calledMethod": "getCities",
        "methodProperties": {
            "AreaRef": area_ref
        }
    }
    response = requests.post(BASE_URL, json=data)
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        return []

def get_warehouses(city_ref):
    data = {
        "apiKey": API_KEY,
        "modelName": "AddressGeneral",
        "calledMethod": "getWarehouses",
        "methodProperties": {
            "CityRef": city_ref,
        }
    }
    response = requests.post(BASE_URL, json=data)
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        return []
# def get_warehouses(city_ref, warehouse_type="1"):
#     payload = {
#         "apiKey": API_KEY,
#         "modelName": "Address",
#         "calledMethod": "getWarehouses",
#         "methodProperties": {
#             "CityRef": city_ref,
#             "TypeOfWarehouseRed": city_ref  # 1 - відділення, 2 - поштомати
#         }
#     }
#     response = requests.post(BASE_URL, json=payload)
#     return response.json()





def areas(request):
    areas = get_areas()
    return JsonResponse(areas, safe=False)

def cities(request):
    area_ref = request.GET.get('area_ref')
    cities = get_cities(area_ref)
    # for city_ref in cities:
    #     get_warehouses(city_ref['Ref'])
    #     print(city_ref['Ref'])
    return JsonResponse(cities, safe=False)

def warehouses(request):
    city_ref = request.GET.get('city_ref')
    warehouses = get_warehouses(city_ref)
    return JsonResponse(warehouses, safe=False)

# def postmachines_view(request):
#     city_ref = request.GET.get('city_ref')
#     data = get_warehouses(city_ref)  # Для поштоматів
#     return JsonResponse(data)

# def warehouses_view(request, city_ref):
#     city_ref = request.GET.get('city_ref')
#     data = get_warehouses(city_ref, "1")  # Для звичайних відділень
#     return JsonResponse(data)


def validation(request):
    area = request.POST.get('area')
    city = request.POST.get('city')
    location = request.POST.get('location')
    number_of_card = request.POST.get('number_of_card')
    month = request.POST.get('month')
    year = request.POST.get('year')
    cvv = request.POST.get('cvv')
    last_name = request.POST.get('last_name')
    first_name = request.POST.get('first_name')
    middle_name = request.POST.get('middle_name')
    number = request.POST.get('number')
    payment_by_card = request.POST.get('payment_by_card')
    # print(payment_by_card)
    
    
    def validate_number_of_card(number_of_card):
        if number_of_card.isdigit() and len(number_of_card) == 16:
            return True
        else:
            return False
        
    def validate_month(month):
        if month.isdigit() and len(month) == 2:
            return True
        else:
            return False
        
    def validate_year(year):
        if year.isdigit() and len(year) == 2:
            return True
        else:
            return False
        
    def validate_cvv(cvv):
        if cvv.isdigit() and len(cvv) == 3:
            return True
        else:
            return False
        
    def validate_last_name(last_name):
        if last_name.isalpha() and len(last_name) <= 50:
            return True
        else:
            return False
    
    def validate_first_name(first_name):
        if first_name.isalpha() and len(first_name) <= 50:
            return True
        else:
            return False

    def validate_middle_name(middle_name):
        if middle_name.isalpha() and len(middle_name) <= 50:
            return True
        else:
            return False
    
    def validate_number(number):
        if number.isdigit() and len(number) == 9:
            return True
        else:
            return False
    
    error = None
    
    
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
        session_key = request.session.session_key
        
    try:
        cart = Cart.objects.get(sessionkey=session_key)
    except:
        cart = Cart.objects.create(sessionkey=session_key)
    
    if payment_by_card == 'true':
        if area and city and location and number_of_card and month and year and cvv and last_name and first_name and middle_name and number:
            if validate_number_of_card(number_of_card):
                if validate_month(month):
                    if validate_year(year):
                        if validate_cvv(cvv):
                            if validate_last_name(last_name):
                                if validate_first_name(first_name):
                                    if validate_middle_name(middle_name):
                                        if validate_number(number):
                                            orders = Orders.objects.get(username=request.user.username)
                                            print(orders)
                                            order = Order.objects.create(orders=orders)
                                            products = cart.productincart_set.all().values()
                                            products = list(products)
                                            for product in products:
                                                # print(product)
                                                product_obj = Product.objects.get(id=product['product_id'])
                                                flavour_obj = Flavour.objects.get(id=product['flavour_id'])
                                                product_in_order = ProductInOrder.objects.create(product=product_obj, order=order, count=product['count'], flavour=flavour_obj)
                                            print(ProductInOrder.objects.all())
                                            cart.delete()
                                            return HttpResponse(100)
                                            
                                        else:
                                            error = 9
                                            return HttpResponse(error)
                                    else:
                                        error = 8
                                        return HttpResponse(error)
                                else:
                                    error = 7
                                    return HttpResponse(error)
                            else:
                                error = 6
                                return HttpResponse(error)
                        else:
                            error = 5
                            return HttpResponse(error)
                    else:
                        error = 4
                        return HttpResponse(error)
                else:
                    error = 3
                    return HttpResponse(error)
            else:
                error = 2
                return HttpResponse(error)
        else:
            error = 1
            return HttpResponse(error)
    elif payment_by_card == 'false':
        if area and city and location and number_of_card and month and year and cvv and last_name and first_name and middle_name and number:
            if validate_last_name(last_name):
                if validate_first_name(first_name):
                    if validate_middle_name(middle_name):
                        if validate_number(number):
                            return HttpResponse(100)
                        else:
                            error = 9
                            return HttpResponse(error)
                    else:
                        error = 8
                        return HttpResponse(error)
                else:
                    error = 7
                    return HttpResponse(error)
            else:
                error = 6
                return HttpResponse(error)
        else:
            error = 1
            return HttpResponse(error)
