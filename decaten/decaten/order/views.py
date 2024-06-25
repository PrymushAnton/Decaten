from django.shortcuts import render, HttpResponse
from .forms import UserInfoForm, PostInfoForm, PaymentForm
# Create your views here.

def order_page(request):
    if request.method == 'POST':
        context = {}
        print(request.POST)
        if request.POST.get('user_info'):
            form = UserInfoForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                surname = form.cleaned_data['surename']
                number = form.cleaned_data['number']

                context = "dict_items([('sUser', ['']))])"
            else:
                context = form.errors.items()
                print(context)

        elif request.POST.get('post_info'):
            form = PostInfoForm(request.POST)
            
            if form.is_valid():
                post = form.cleaned_data['post']
                sending_option = form.cleaned_data['sending_option']
                address = form.cleaned_data['address']
                post_index = form.cleaned_data['post_index']
                
                context = "dict_items([('sPost', ['']))])"
            else:
                context = form.errors.items()
        elif request.POST.get('pay_info'):
            form = PaymentForm(request.POST)
        # post = request.POST.get("post")
        # sending_option = request.POST.get("sending_option")
        # address = request.POST.get("address")
        # post_index = request.POST.get("post_index")
        return HttpResponse(context)
    else:
        return render(request, 'order/order_page.html')
    