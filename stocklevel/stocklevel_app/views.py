from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from .models import Component, Supplier, Product, Recipient, WarehouseFlows

from .forms import ComponentForm, ProductForm, SupplierForm, RecipientForm, WarehouseEntryForm,\
    WarehouseReleaseForm, WarehouseEntryLaboratoryForm


class BaseView(View):
    def get(self, request):
        return render(request, 'base.html')


class ComponentCreateView(CreateView):
    model = Component
    fields = ['name', 'measure']
    success_url = '/components/'


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
    success_url = '/suppliers/'


class ComponentsView(View):
    def get(self, request):
        components = Component.objects.all()
        return render(request, 'components.html', {'components': components})


class ComponentView(View):
    def get(self, request, component_id):
        component = Component.objects.get(id=component_id)
        return render(request, 'component.html', {'component': component})


class SuppliersView(View):
    def get(self, request):
        suppliers = Supplier.objects.all()
        return render(request, 'suppliers.html', {'suppliers': suppliers})


class SupplierView(View):
    def get(self, request, supplier_id):
        supplier = Supplier.objects.get(id=supplier_id)
        components = supplier.component.all()
        return render(request, 'supplier.html', {'supplier': supplier, 'components': components})


# nowa rzecz 01.02.2021
class WarehouseEntryCreate(CreateView):
    form_class = WarehouseEntryForm
    model = WarehouseFlows
    success_url = '/stock-level/'

    def form_valid(self, form):
        new_entry = form.save()
        component = form.cleaned_data['component']
        component.stock_level += int(form.cleaned_data['series_amount'])
        new_comp = component.save()
        return redirect('/stock-level/')


# działa z walidacją w forms.py
class WarehouseReleaseView(UpdateView):
    form_class = WarehouseReleaseForm
    model = WarehouseFlows
    template_name_suffix = '_update_form'

    def form_valid(self, form):
        component = form.cleaned_data['component']
        component.stock_level -= int(form.cleaned_data['release_amount'])
        new_component = component.save()
        new_release = form.save()
        new_release.series_amount -= int(form.cleaned_data['release_amount'])
        new_release.save()
        return redirect('/stock-level/')


class AddLaboratoryNumberView(UpdateView):
    model = WarehouseFlows
    form_class = WarehouseEntryLaboratoryForm
    template_name_suffix = '_update_form'
    success_url = '/stock-level/'


class AllEntriesView(View):
    def get(self, request):
        entries = WarehouseFlows.objects.all().order_by('delivery_date')
        return render(request, 'all_entries.html', {'entries': entries})


class StockLevelView(View):
    def get(self, request):
        components = Component.objects.all().order_by('name')
        return render(request, 'stock_level.html', {'components': components})


class SupplierUpdate(UpdateView):
    model = Supplier
    fields = ['comment', 'category']
    template_name_suffix = '_update_form'
    success_url = '/suppliers/'
