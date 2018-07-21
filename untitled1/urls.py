"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from axf import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('home/', views.home),
    path('market/', views.market),
    # path('selmarket/<str:categoryid>/<str:cid>/<int:sortid>/', views.selmarket),
    path('shopcar/', views.shopcar),
    path('addgoods/', views.add_goods),
    path('subgoods/', views.sub_goods),
    path('mine/', views.mine),
    path('login/', views.login),
    path('login_check/', views.login_check),
    path('namecheck/', views.namecheck),
    # path('initall/', views.init_all),
    path('issele/', views.issele),
    path('order/', views.order),

    path('userrole/', views.user_role)


]
