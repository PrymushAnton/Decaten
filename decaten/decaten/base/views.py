from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'base/base.html')

def support_chat(request):
    return render(request, "base/support.html")