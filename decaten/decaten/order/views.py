from django.shortcuts import render

# Create your views here.

def order_page(request):
    if request.method == 'POST':
        print(request.POST)
        post = request.POST.get("post")
        sending_option = request.POST.get("sending_option")
        address = request.POST.get("address")
        post_index = request.POST.get("post_index")
        
    return render(request, 'order/order_page.html')