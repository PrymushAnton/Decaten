from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import UserInfo
from django.http import HttpResponse

# Create your views here.
def reg_page(request):
    if request.user.is_authenticated:
        return redirect('main')
    context = {'fotti':True}
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     email = request.POST.get('email')
    #     region = request.POST.get('region')
    #     number = request.POST.get('number')
    #     password = request.POST.get('password')
    #     password_confirmation = request.POST.get('password_confirmation')
    #     if username and email and region and number and password and password_confirmation:
    #         try:
    #             cheak_email = User.objects.get(email=email)
    #         except:
    #             cheak_email = None
    #         finally:
    #             if not cheak_email:
    #                 if password == password_confirmation:
    #                     try:
    #                         num = int(region + number)
    #                         try:
    #                             user = User.objects.create_user(username=username, email=email, password=password)
    #                             UserInfo.objects.create(user_id=user, number=num)
    #                             login(request, user)
    #                             return redirect('main')
    #                         except:
    #                             pass
    #                     except:
    #                         pass
    return render(request, 'user/reg.html', context)



def log_page(request):
    if request.user.is_authenticated:
        return redirect('main')
    context = {'fotti':True}
    # if request.method == 'POST':
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     if email and password:
    #         user = User.objects.get(email = email)
    #         if user.check_password(password):
    #             login(request, user)
    #             return redirect('main')
    #         else:
    #             error = 'Неправильний пароль!'
    #             error = 2
    #             return HttpResponse(error)
    #     else:
    #         error = 'Заповніть це поле!'
    #         error = 1
    #         return HttpResponse(error)
    return render(request, 'user/log.html', context)

def logout_page(request):
    logout(request)
    return redirect('main')

def log_in_account(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:
            try:
                user = User.objects.get(email = email)
                if user.check_password(password):
                    login(request, user)
                    
                    # return redirect('main')
                    # success = 'Ви зареєстровані!'
                    success = 5
                    return HttpResponse(success)
                else:
                    error = 'Неправильний пароль!'
                    error = 2
                    return HttpResponse(error)
            except:
                error = 'Пошта не зареєстрована!'
                error = 4
                return HttpResponse(error)
            
        else:
            error = 'Заповніть це поле!'
            error = 1
            return HttpResponse(error)
    return HttpResponse()

def validate_account(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        region = request.POST.get('region')
        number = request.POST.get('number')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')
        # and region 
        print(username, email, password, password_confirmation)
        if username and email and number and password and password_confirmation:
            try:
                check_email = User.objects.get(email=email)
            except:
                check_email = None
            finally:
                if not check_email:
                    if password == password_confirmation:
                        
                        try:
                            user = User.objects.create_user(username=username, email=email, password=password)
                            UserInfo.objects.create(user_id=user, number=number)
                            login(request, user)
                            print(1235345345345345)
                            # print(user.is_authenticated())
                            success = 5
                            return HttpResponse(success)
                            # return redirect('main')
                        except:
                            error = 'Помилка! Спробуйте пізніше!'
                            error = 4
                            return HttpResponse(error)
                        # try:
                        #     num = int(region + number)
                            
                        # except:
                        #     pass
                    else:
                        error = 'Паролі не співпадають!'
                        error = 3
                        return HttpResponse(error)
                else:
                    error = 'Дана пошта вже використовується!'
                    error = 2
                    return HttpResponse(error)
        else:
            error = 'Заповніть це поле!'
            error = 1
            return HttpResponse(error)
    # success = 'Success'
    # return HttpResponse(success)