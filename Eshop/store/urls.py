"""
URL configuration for Eshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path
from . import views
from .views import Login,Signup,Index,Cart,CheckOut,OrderView
#from .middleware.auth import auth_middleware

urlpatterns = [
   #path('',views.index,name='homepage'),
   path('',Index.as_view(),name='homepage'),
   path('signup/',Signup.as_view(),name='signup'),
   path('login/',Login.as_view(),name='login'),
   path('logout/',views.logout,name='logout'),
   path('cart/',Cart.as_view(),name='cart'),
   path('check-out',CheckOut.as_view(),name='checkout'),
   #path('orders/',auth_middleware(OrderView.as_view()),name='orders')
   path('orders/',OrderView.as_view(),name='orders'),
   path('search/',views.search,name='search'),

]
