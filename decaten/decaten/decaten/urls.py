"""
URL configuration for decaten project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from decaten.settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from main.views import *
from base.views import *
from user.views import log_page, reg_page,logout_page, validate_account, log_in_account
from catalog_product.views import *
from cart.views import *
from order.views import *
from my_order.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    # path('base/', base, name='base'),
    path('login/', log_page, name='log'),
    path('registration/', reg_page, name='reg'),
    path('logout/', logout_page, name='logout'),
    path('validate_account/', validate_account, name='validate_account'),
    path('log_in_account/', log_in_account, name='log_in_account'),
    path('catalog/', catalog, name='catalog'),
    path('catalog/filter_products/', filter_products, name='filter_products'),
    path('catalog/get_flavour_image/', get_flavour_image, name='get_flavour_image'),
    path('catalog/product_image/', product_image, name='product_image'),
    path('product/<id>/', product_page, name='product_page'),
    path('product_flavour_main/', product_flavour_main, name='product_flavour_main'),
    path('product_image_main/', product_image_main, name='product_image_main'),
    path('get_flavour_image/', get_flavour_image, name='product_page'),
    path('cart/', cart, name='cart'),

    path('cart/plus_count/', plus_count, name='plus_count'),
    path('cart/minus_count/', minus_count, name='minus_count'),
    path('cart/delete_product/', delete_product, name='delete_product'),
    path('add_to_cart/', add_to_cart, name='product_page'),
    path('cart/error_empty/', error_empty, name='error_empty'),

    path('order', order_page,name='order'),
    path('my_order/', my_order, name='my_order'),
    path('orders/', orders, name='orders'),
    
    # path('cart/get_flavour_image/', get_flavour_image_cart, name='get_flavour_image_Cart'),

    path('areas/', areas, name='areas'),
    path('cities/', cities, name='cities'),
    path('warehouses/', warehouses, name='warehouses'),
    path('validation/', validation, name='validation'),
    
    
    # path('count_cart/', count_cart, name='count_cart'),
    path('order/<id>/', order, name='order'),
    path('cancel_order/', cancel_order, name='cancel_order'),
    path('sent_order/', sent_order, name='sent_order'),
    path('arrived_order/', arrived_order, name='arrived_order'),
    path('success_order/', success_order, name='success_order'),
    

]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)