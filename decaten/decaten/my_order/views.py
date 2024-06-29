from django.shortcuts import render, redirect
import requests
from django.http import JsonResponse, HttpResponse
from .models import *
from catalog_product.models import *
from django.contrib.auth import authenticate
from datetime import date
from cart.models import *

API_KEY = 'a82d9d12e5f74a8692792b6930d55bc4'
BASE_URL = 'https://api.novaposhta.ua/v2.0/json/'

def cancel_order(request):
    id = request.POST.get('id')
    order = Order.objects.get(id=id)
    
    products = order.productinorder_set.all().values()
    products = list(products)
    for product in products:
        # print(product)
        flavour = Flavour.objects.get(id=product['flavour_id'])
        flavour.count_of_product = int(flavour.count_of_product) + int(product['count'])
        flavour.save()
    
    # print(id)
    
    order.status = 0
    order.save()
    
    return HttpResponse()

def sent_order(request):
    id = request.POST.get('id')
    # print(id)
    order = Order.objects.get(id=id)
    order.status = 2
    order.save()
    
    return HttpResponse()

def arrived_order(request):
    id = request.POST.get('id')
    # print(id)
    order = Order.objects.get(id=id)
    order.status = 3
    order.save()
    return HttpResponse()

def success_order(request):
    id = request.POST.get('id')
    # print(id)
    order = Order.objects.get(id=id)
    order.status = 4
    order.save()
    return HttpResponse()

def order(request, id):
    # print(id)

    context = {}
    try:
        order = Order.objects.get(id=id)
        # print(order)
        products_in_order = ProductInOrder.objects.filter(order_id=order.id)
        
        products = ProductInOrder.objects.filter(order=order).values()
        products = list(products)
        # print(products)
        list_of_ids = []
        list_of_ids_for_flavours = []
        list_of_prices = []
        list_of_counts = []
        list_of_final_prices = []
        for product in products:
            list_of_ids.append(product['product_id'])
            list_of_ids_for_flavours.append(product['flavour_id'])
            list_of_counts.append(product['count'])
        print(list_of_counts)
        all_products_for_prices = Product.objects.filter(id__in=list_of_ids).values()
        all_products_for_prices = list(all_products_for_prices)
        # print('all',all_products_for_prices)
        for product in all_products_for_prices:
            list_of_prices.append(product['price'])
        # print(list_of_prices)
        count = 0
        for price in list_of_prices:
            list_of_final_prices.append(int(price)*int(list_of_counts[count]))
            count += 1
            
        # print(list_of_final_prices)
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
            
        
        # all_products = Product.objects.filter(id__in=list_of_ids)
        all_products = []
        all_flavours = Flavour.objects.filter(id__in=list_of_ids_for_flavours).values()
        all_flavours = list(all_flavours)
        print(all_flavours)
        list_of_products = []
        list_of_products_prices = []
        count_for_price = 0
        for flavour in all_flavours:
            product = Product.objects.get(id=flavour['for_product_id'])
            list_of_products.append(product)
            list_of_products_prices.append(int(product.price) * int(list_of_counts[count_for_price]))
            count_for_price += 1
        print(list_of_products)
        
        print(list_of_products_prices)
        flavours = Flavour.objects.filter(id__in=list_of_ids_for_flavours)
            
        # print(all_flavours)
        context = {'products': list_of_products, 'flavours': flavours, 'products_in_order': products_in_order, 'prices': list_of_products_prices, 'count_cart': count}
        # print(list(products))
    except:
        print('except')
    
    
    
    return render(request, 'my_order/order.html', context)

def orders(request):
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
        
        
        
    if not request.user.is_staff:
        orders = Orders.objects.get(username=request.user.username)
        
        all_orders = Order.objects.filter(orders=orders)

        date_today = date.today()
        date_today = str(date_today).split('-')

        
        
        context = {'all_orders': all_orders, 'count_cart': count}
    elif request.user.is_staff:
        all_orders_of_users = Order.objects.all()
        context = {'count_cart': count, 'all_orders_of_users': all_orders_of_users}
    
    
    
    
    
    
    
    
    return render(request, 'my_order/orders.html', context)

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
    # products = []
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
        
    
    context = {'price':price_of_order, 'count_cart': count}
    
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
    print(area, city, location)
    
    def validate_area(area):
        if area[0] != 'О':
            return True
        else:
            return False
    
    def validate_city(city):
        if city[0] != 'О':
            return True
        else:
            return False   
    
    def validate_location(location):
        if location[0] != 'О':
            return True
        else:
            return False
    
    def validate_number_of_card(number_of_card):
        if number_of_card.isdigit() and len(str(number_of_card)) == 16:
            return True
        else:
            return False
        
    def validate_month(month):
        if month.isdigit() and len(str(month)) == 2:
            if int(month) <= 12 and int(month) >= 1:
                return True
            else:
                return False
        else:
            return False
        
    def validate_year(year):
        if year.isdigit() and len(str(year)) == 2:
            if int(year) >= 24 and int(year) <= 29:
                return True
            else:
                return False
        else:
            return False
        
    def validate_cvv(cvv):
        if cvv.isdigit() and len(str(cvv)) == 3:
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
        
        
    price_of_order = 0
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
    
    if request.user.is_authenticated:
        if area and city and location and number_of_card and month and year and cvv and last_name and first_name and middle_name and number:
            if validate_area(area):
                if validate_city(city):
                    if validate_location(location):
                        if validate_number_of_card(number_of_card):
                            if validate_month(month):
                                if validate_year(year):
                                    if validate_cvv(cvv):
                                        if validate_last_name(last_name):
                                            if validate_first_name(first_name):
                                                if validate_middle_name(middle_name):
                                                    if validate_number(number):
                                                        orders = Orders.objects.get(username=request.user.username)
                                                        # print()
                                                        date_today = date.today()
                                                        date_today = str(date_today).split('-')
                                                        
                                                        order = Order.objects.create(orders=orders, status=1, price = price_of_order, area=area, city=city, location=location, day_num=date_today[2], month_num=date_today[1], year_num=date_today[0], number_of_card=number_of_card, month=month, year=year, cvv=cvv, last_name=last_name, first_name=first_name, middle_name=middle_name, number=number)
                                                        products = cart.productincart_set.all().values()
                                                        products = list(products)
                                                        for product in products:
                                                            # print(product)
                                                            product_obj = Product.objects.get(id=product['product_id'])
                                                            flavour_obj = Flavour.objects.get(id=product['flavour_id'])
                                                            product_in_order = ProductInOrder.objects.create(product=product_obj, order=order, count=product['count'], flavour=flavour_obj)
                                                            flavour = Flavour.objects.get(id=product['flavour_id'])
                                                            flavour.count_of_product = int(flavour.count_of_product) - int(product['count'])
                                                            flavour.save()
                                                            
                                                            
                                                            
                                                            
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
                        return HttpResponse(12)
                else:
                    return HttpResponse(11)
            else:
                return HttpResponse(10)
        else:
            error = 1
            return HttpResponse(error)
    else:
        return HttpResponse(321)
    #     elif payment_by_card == 'false':
    #         if area and city and location and last_name and first_name and middle_name and number:
    #             if validate_area(area):
    #                 if validate_city(city):
    #                     if validate_location(location):
    #                         if validate_last_name(last_name):
    #                             if validate_first_name(first_name):
    #                                 if validate_middle_name(middle_name):
    #                                     if validate_number(number):
    #                                         orders = Orders.objects.get(username=request.user.username)
    #                                         # print()
    #                                         date_today = date.today()
    #                                         date_today = str(date_today).split('-')
                                            
    #                                         order = Order.objects.create(orders=orders, status=1, price = price_of_order, area=area, city=city, location=location, day_num=date_today[2], month_num=date_today[1], year_num=date_today[0])
    #                                         products = cart.productincart_set.all().values()
    #                                         products = list(products)
    #                                         for product in products:
    #                                             # print(product)
    #                                             product_obj = Product.objects.get(id=product['product_id'])
    #                                             flavour_obj = Flavour.objects.get(id=product['flavour_id'])
    #                                             product_in_order = ProductInOrder.objects.create(product=product_obj, order=order, count=product['count'], flavour=flavour_obj)
    #                                             flavour = Flavour.objects.get(id=product['flavour_id'])
    #                                             print(int(product['count']))
    #                                             flavour.count_of_product -= int(product['count'])
    #                                             flavour.save()
    #                                         print(ProductInOrder.objects.all())
    #                                         cart.delete()
    #                                         return HttpResponse(100)
    #                                     else:
    #                                         error = 9
    #                                         return HttpResponse(error)
    #                                 else:
    #                                     error = 8
    #                                     return HttpResponse(error)
    #                             else:
    #                                 error = 7
    #                                 return HttpResponse(error)
    #                         else:
    #                             error = 6
    #                             return HttpResponse(error)
    #                     else:
    #                         return HttpResponse(12)
    #                 else:
    #                     return HttpResponse(11)
    #             else:
    #                 return HttpResponse(10)
    #         else:
    #             error = 1
    #             return HttpResponse(error)


