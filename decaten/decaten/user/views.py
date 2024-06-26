from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import MyUser
from django.contrib.auth import authenticate, login, logout
from .models import UserInfo
from django.http import HttpResponse
import re
from catalog_product.models import *

def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(regex, email):
        return True
    else:
        return False
    
def validate_number(number):
    if number.isdigit() and len(number) == 9:
        return True
    else:
        return False
    

def validate_first_name(first_name):
    if first_name.isalpha():
        return True
    else:
        return False
    
def validate_first_name_len(first_name):
    if len(first_name) <= 12:
        return True
    else:
        return False
    
def validate_last_name_len(last_name):
    if len(last_name) <= 12:
        return True
    else:
        return False

    
def validate_last_name(last_name):
    if last_name.isalpha():
        return True
    else:
        return False
    
def validate_password(password):
    if len(password) >= 8:
        return True
    else:
        return False
    
def validate_password_confirmation(password, password_confirmation):
    if password == password_confirmation:
        return True
    else:
        return False
    
    
# Create your views here.
def reg_page(request):
    if request.user.is_authenticated:
        return redirect('main')
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
        session_key = request.session.session_key
        
    try:
        cart = Cart.objects.get(sessionkey=session_key)
    except:
        cart = Cart.objects.create(sessionkey=session_key)

    count = 0
    for product in cart.productincart_set.all():
        product_obj = Product.objects.filter(id=product.product_id).values()
        product_obj = list(product_obj)
        count += product.count
        
    context = {'fotti':True, 'count_cart':count}
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
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
        session_key = request.session.session_key
        
    try:
        cart = Cart.objects.get(sessionkey=session_key)
    except:
        cart = Cart.objects.create(sessionkey=session_key)

    count = 0
    for product in cart.productincart_set.all():
        product_obj = Product.objects.filter(id=product.product_id).values()
        product_obj = list(product_obj)
        count += product.count
        
    context = {'fotti':True,'count_cart': count,}
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
                user = MyUser.objects.get(email=email)
                
                if user.check_password(password):
                    login(request, user)
                    success = 4
                    return HttpResponse(success)
                else:
                    error = 'Неправильний пароль!'
                    error = 3
                    return HttpResponse(error)
            except:
                error = 'Пошта не зареєстрована!'
                error = 2
                return HttpResponse(error)
        else:
            error = 'Заповніть це поле!'
            error = 1
            return HttpResponse(error)    
            
            
            # try:
            #     user = User.objects.get(email = email)
            #     if user.check_password(password):
                    
            #         login(request, user)
                    
            #         # return redirect('main')
            #         # success = 'Ви зареєстровані!'
            #         success = 5
            #         return HttpResponse(success)
            #     else:
            #         error = 'Неправильний пароль!'
            #         error = 2
            #         return HttpResponse(error)
            # except:
            #     error = 'Пошта не зареєстрована!'
            #     error = 4
            #     return HttpResponse(error)

        
        
        
        # try:
        #         user = User.objects.get(email = email_or_phone)
        #         if user.check_password(password):
                    
        #             login(request, user)
                    
        #             # return redirect('main')
        #             # success = 'Ви зареєстровані!'
        #             success = 5
        #             return HttpResponse(success)
        #         else:
        #             error = 'Неправильний пароль!'
        #             error = 2
        #             return HttpResponse(error)
        #     except:
        #         error = 'Пошта не зареєстрована!'
        #         error = 4
        #         return HttpResponse(error)
        

def validate_account(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        # region = request.POST.get('region')
        number = request.POST.get('number')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')
        # and region 
        print(first_name, last_name, email, number, password, password_confirmation)
        if first_name and last_name and email and number and password and password_confirmation:
            if validate_first_name(first_name):
                if validate_first_name_len(first_name):
                    if validate_last_name(last_name):
                        if validate_last_name_len(last_name):
                            if validate_email(email):
                                try:
                                    check_email = MyUser.objects.get(email=email)
                                except:
                                    check_email = None
                                finally:
                                    if not check_email:
                                        if validate_number(number):
                                            try:
                                                check_number = MyUser.objects.get(email=email)
                                            except:
                                                check_number = None
                                            finally:
                                                if not check_number:
                                                    if validate_password(password):
                                                        if validate_password_confirmation(password, password_confirmation):
                                                            try:
                                                                user = MyUser.objects.create_user(username=first_name,first_name=first_name, last_name=last_name, email=email, number=number, password=password)
                                                                login(request, user)
                                                                success = 10
                                                                return HttpResponse(success)
                                                            except:
                                                                error = 9
                                                                return HttpResponse(error)
                                                        else:
                                                            error = 'Паролі не співпадають!'
                                                            error = 8
                                                            return HttpResponse(error)
                                                    else:
                                                        error = 'У паролі повинно бути 8 або більше символів!'
                                                        error = 7
                                                        return HttpResponse(error)
                                                else:
                                                    error = 'Даний номер телефону вже використовується!'
                                                    error = 6
                                                    return HttpResponse(error)
                                        else:
                                            error = 'Не вірно введений номер телефону!'
                                            error = 5
                                            return HttpResponse(error)
                                    else:
                                        error = 'Дана пошта вже використовується!'
                                        error = 4
                                        return HttpResponse(error)
                            else:
                                error = 'Введіть коректну пошту!'
                                error = 3
                                return HttpResponse(error)
                        else:
                            error = "Прізвище не повинно бути більше 15 символів!"
                            error = 13
                            return HttpResponse(error)
                    else:
                        error = "В прізвищі не повинні бути цифри або спец. символи!"
                        error = 11
                        return HttpResponse(error)
                else:
                    error = "Ім'я не повинно бути більше 12 символів!"
                    error = 12
                    return HttpResponse(error)
            else:
                error = "В імені не повинні бути цифри або спец. символи!"
                error = 2
                return HttpResponse(error)
        else:
            error = 'Заповніть це поле!'
            error = 1
            return HttpResponse(error)
                                    
                    
            
            
            
            
        #     try:
        #         check_email = User.objects.get(email=email)
        #     except:
        #         check_email = None
        #     finally:
        #         if not check_email:
        #             if validate_email(email=email):
        #                 print('email')
        #                 if validate_number(number):
        #                     if password == password_confirmation:
        #                         print('password')
        #                         try:
        #                             user = User.objects.create_user(username=username, email=email, password=password)
        #                             UserInfo.objects.create(user_id=user, number=number)
        #                             login(request, user)
        #                             print('reg')
        #                             # print(user.is_authenticated())
        #                             success = 5
        #                             return HttpResponse(success)
        #                             # return redirect('main')
        #                         except:
        #                             error = 'Помилка! Спробуйте пізніше!'
        #                             error = 4
        #                             return HttpResponse(error)
        #                         # try:
        #                         #     num = int(region + number)
                                    
        #                         # except:
        #                         #     pass
        #                     else:
        #                         error = 'Паролі не співпадають!'
        #                         error = 3
        #                         return HttpResponse(error)
        #                 else:
        #                     error = 7
        #                     return HttpResponse(error)
        #             else:
        #                 error = 6
        #                 return HttpResponse(error)
                        
        #         else:
        #             error = 'Дана пошта вже використовується!'
        #             error = 2
        #             return HttpResponse(error)
        # else:
        #     error = 'Заповніть це поле!'
        #     error = 1
        #     return HttpResponse(error)
    # success = 'Success'
    # return HttpResponse(success)
    
    
    
    
    
# if username and email and number and password and password_confirmation:
#             try:
#                 check_email = User.objects.get(email=email)
#             except:
#                 check_email = None
#             finally:
#                 if not check_email:
#                     if validate_email(email=email):
#                         print('email')
#                         if validate_number(number):
#                             if password == password_confirmation:
#                                 print('password')
#                                 try:
#                                     user = User.objects.create_user(username=username, email=email, password=password)
#                                     UserInfo.objects.create(user_id=user, number=number)
#                                     login(request, user)
#                                     print('reg')
#                                     # print(user.is_authenticated())
#                                     success = 5
#                                     return HttpResponse(success)
#                                     # return redirect('main')
#                                 except:
#                                     error = 'Помилка! Спробуйте пізніше!'
#                                     error = 4
#                                     return HttpResponse(error)
#                                 # try:
#                                 #     num = int(region + number)
                                    
#                                 # except:
#                                 #     pass
#                             else:
#                                 error = 'Паролі не співпадають!'
#                                 error = 3
#                                 return HttpResponse(error)
#                         else:
#                             error = 7
#                             return HttpResponse(error)
#                     else:
#                         error = 6
#                         return HttpResponse(error)
                        
#                 else:
#                     error = 'Дана пошта вже використовується!'
#                     error = 2
#                     return HttpResponse(error)
#         else:
#             error = 'Заповніть це поле!'
#             error = 1
#             return HttpResponse(error)