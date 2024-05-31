from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import UserInfo

# Create your views here.
def reg_page(request):
    if request.user.is_authenticated:
        return redirect('main')
    context = {'fotti':True}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        region = request.POST.get('region')
        number = request.POST.get('number')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')
        if username and email and region and number and password and password_confirmation:
            try:
                cheak_email = User.objects.get(email=email)
            except:
                cheak_email = None
            finally:
                if not cheak_email:
                    if password == password_confirmation:
                        try:
                            num = int(region + number)
                            try:
                                user = User.objects.create_user(username=username, email=email, password=password)
                                UserInfo.objects.create(user_id=user, number=num)
                                login(request, user)
                                return redirect('main')
                            except:
                                pass
                        except:
                            pass
    return render(request, 'user/reg.html', context)



def log_page(request):
    if request.user.is_authenticated:
        return redirect('main')
    context = {'fotti':True}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:
            user = User.objects.get(email = email)
            if user.check_password(password):
                login(request, user)
                return redirect('main')
    return render(request, 'user/log.html', context)

def logout_page(request):
    logout(request)
    return redirect('main')