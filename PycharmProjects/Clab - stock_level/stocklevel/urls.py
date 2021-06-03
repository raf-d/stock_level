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
from stocklevel_app.views import BaseView, ComponentCreateView, ProductCreateView, \
    RecipientCreateView, SupplierCreateView, ComponentsView, ComponentView, SuppliersView, \
    SupplierView, WarehouseEntryCreate, WarehouseReleaseView, StockLevelView, SupplierUpdate, \
    AddLaboratoryNumberView, AllEntriesView, EntryDetailedView, LoginView, LogoutView, ProductsView,\
    ProductView, ProductUpdate, RecipientsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('', BaseView.as_view()),
    path('add-component/', ComponentCreateView.as_view()),
    path('add-product/', ProductCreateView.as_view()),
    path('add-recipient/', RecipientCreateView.as_view()),
    path('add-supplier/', SupplierCreateView.as_view()),
    path('update-supplier/<int:pk>/', SupplierUpdate.as_view()),
    path('components/', ComponentsView.as_view()),
    path('component/<int:component_id>/', ComponentView.as_view()),
    path('suppliers/', SuppliersView.as_view()),
    path('supplier/<int:supplier_id>/', SupplierView.as_view()),
    path('products/', ProductsView.as_view()),
    path('product/<int:product_id>/', ProductView.as_view()),
    path('recipients/', RecipientsView.as_view()),
    path('update-product/<int:pk>/', ProductUpdate.as_view()),
    path('add-warehouse-entry/', WarehouseEntryCreate.as_view()),
    path('entry-detailed-view/<int:entry_id>/', EntryDetailedView.as_view()),
    path('add-laboratory-number/<int:pk>/', AddLaboratoryNumberView.as_view()),
    path('all-entries-view/', AllEntriesView.as_view()),
    path('add-warehouse-release/<int:pk>/', WarehouseReleaseView.as_view()),
    path('stock-level/', StockLevelView.as_view()),

]
