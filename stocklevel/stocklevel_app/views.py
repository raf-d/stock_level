from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from .models import Component, Supplier, Product, Recipient, WarehouseEntry, WarehouseRelease
from .forms import ComponentForm, ProductForm, SupplierForm, RecipientForm, WarehouseEntryForm, WarehouseReleaseForm


# Create your views here.
class BaseView(View):
    def get(self, request):
        return render(request, 'base.html')


class ComponentCreateView(CreateView):
    model = Component
    fields = '__all__'
    success_url = '/'


class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    success_url = '/'


class RecipientCreateView(CreateView):
    model = Recipient
    fields = '__all__'
    success_url = '/'


class SupplierCreateView(CreateView):
    model = Supplier
    fields = '__all__'
    success_url = '/'


class ComponentsView(View):
    def get(self, request):
        components = Component.objects.all()
        return render(request, 'components.html', {'components': components})


class ComponentView(View):
    def get(self, request, component_id):
        component = Component.objects.get(id=component_id)
        return render(request, 'component.html', {'component': component})



# class ComponentCreateView(View):
#     def get(self, request):
#         form = ComponentForm()
#         return render(request, 'component_form.html', {'form': form})
#
#     def post(self, request):
#         pass