from django.shortcuts import render
from .models import Carusel

# Create your views here.
def main(request):
    context = {}
    images_for_carusel = Carusel.objects.all()
    context['images_for_carusel'] = images_for_carusel
    return render(request, 'main/main.html', context)