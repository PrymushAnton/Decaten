from django.shortcuts import render
import requests
from django.http import JsonResponse

API_KEY = 'a82d9d12e5f74a8692792b6930d55bc4'
BASE_URL = 'https://api.novaposhta.ua/v2.0/json/'


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
            "CityRef": city_ref
        }
    }
    response = requests.post(BASE_URL, json=data)
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        return []



def my_order(request):
    
    # cities = get_cities()
    # print(cities)
    context = {}
    
    return render(request, 'my_order/my_order.html', context)

def areas(request):
    areas = get_areas()
    return JsonResponse(areas, safe=False)

def cities(request):
    area_ref = request.GET.get('area_ref')
    cities = get_cities(area_ref)
    return JsonResponse(cities, safe=False)

def warehouses(request):
    city_ref = request.GET.get('city_ref')
    warehouses = get_warehouses(city_ref)
    return JsonResponse(warehouses, safe=False)