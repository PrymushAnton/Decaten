from django.shortcuts import render

# Create your views here.
def reg_page(request):
    context = {'fotti':True}
    return render(request, 'user/reg.html', context)



def log_page(request):
    context = {'fotti':True}
    return render(request, 'user/log.html', context)