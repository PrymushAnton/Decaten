from django.shortcuts import render

# Create your views here.

def order_page(request):
    return render(request, 'order/order_page.html')