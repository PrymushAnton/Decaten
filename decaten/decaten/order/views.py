from django.shortcuts import render, HttpResponse
from .forms import UserInfoForm, PostInfoForm
# Create your views here.

def order_page(request):
    if request.method == 'POST':
        context = {}
        if request.POST.get('user_info'):
            form = UserInfoForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                surname = form.cleaned_data['surename']
                number = form.cleaned_data['number']

                context = "dict_items([('sUser', ['']))])"
            else:
                print(1)
                context = form.errors.items()
                print(context)

        elif request.POST.get('post_info'):
            form = PostInfoForm(request.POST)
            if form.is_valid():
                post = form.cleaned_data['post']
                sending_option = form.cleaned_data['sending_option']
                address = form.cleaned_data['address']
                post_index = form.cleaned_data['post_index']
                print(1)
            else:
                context = form.non_field_errors()
        elif request.POST.get('pay_info'):
            pass
        # post = request.POST.get("post")
        # sending_option = request.POST.get("sending_option")
        # address = request.POST.get("address")
        # post_index = request.POST.get("post_index")
        return HttpResponse(context)
    else:
        return render(request, 'order/order_page.html')
    