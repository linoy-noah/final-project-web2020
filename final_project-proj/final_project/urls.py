"""final_project URL Configuration

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
from django.urls import path
from deliveries import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.registerform , name="registerform"),
    path('',views.homepage,name="homepage"),
    path('accounts/login/',views.needlogin,name="needlogin"),
    path('logout/',views.logoutuser, name="logoutuser"),
    path('login/',views.loginuser, name="loginuser"),
    path('order/',views.order,name ='order'),
    path('myDeliveries/',views.myDeliveries,name="myDeliveries"),
    path('myDeliveries/<int:delivery_pk>/',views.showDelivery),
    path('myDeliveries/<int:delivery_pk>/delete/',views.deleteDelivery, name="deleteDelivery"),
    path('makeDelivery/',views.makeDelivery,name="makeDelivery"),
    path('makeDelivery/<int:delivery_pk>/',views.updatestat,name="updatestat")
]
