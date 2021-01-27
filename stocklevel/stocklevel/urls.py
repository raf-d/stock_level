"""stocklevel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from stocklevel_app.views import BaseView, ComponentCreateView, ProductCreateView,\
    RecipientCreateView, SupplierCreateView, ComponentsView, ComponentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BaseView.as_view()),
    path('add-component/', ComponentCreateView.as_view()),
    path('add-product/', ProductCreateView.as_view()),
    path('add-recipient/', RecipientCreateView.as_view()),
    path('add-supplier/', SupplierCreateView.as_view()),
    path('components/', ComponentsView.as_view()),
    path('component/<int:component_id>/', ComponentView.as_view()),
]
