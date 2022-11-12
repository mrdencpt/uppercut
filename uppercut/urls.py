"""uppercut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', include('admin_honeypot.urls'), name='admin_honeypot'),
    #ทำเก็บคนแอบเข้า admin จบบรรทัดนี้ สั่ง python manage.py migrate จะสร้างตารางเก็บADMIN_HONEYPOT
    path('securelogin/', admin.site.urls), # เข้าadmin
    path('', views.home, name='home'),
    path('store/', include('store.urls')),
    path('cart/', include('carts.urls')),
    path('accounts/', include('accounts.urls')),

    #ORDERS
    path('orders/', include('orders.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
