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


class BaseView(View):
    def get(self, request):
        return render(request, 'base.html')


class ComponentCreateView(CreateView):
    model = Component
    fields = ['name', 'measure']
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


class SuppliersView(View):
    def get(self, request):
        suppliers = Supplier.objects.all()
        return render(request, 'suppliers.html', {'suppliers': suppliers})


class SupplierView(View):
    def get(self, request, supplier_id):
        supplier = Supplier.objects.get(id=supplier_id)
        components = supplier.component.all()
        return render(request, 'supplier.html', {'supplier': supplier, 'components': components})


class WarehouseEntryView(View):
    def get(self, request):
        form = WarehouseEntryForm()
        return render(request, 'warehouse_entry.html', {'form': form})

    def post(self, request):
        form = WarehouseEntryForm(request.POST)
        if form.is_valid():
            warehouse_entry = form.save()
            print(request.POST['component'])
            component = Component.objects.get(id=request.POST['component'])
            component.stock_level += int(request.POST['amount'])
            print(component.stock_level)
            new_comp = component.save()
            return redirect('/')
        else:
            return render(request, 'warehouse_entry.html', {'form': form})


class WarehouseReleaseFormView(FormView):  # do uzupełnienia
    def get(self, request):
        form = WarehouseReleaseForm()
        return render(request, 'warehouse_release.html', {'form': form})

    def post(self, request):
        form = WarehouseReleaseForm(request.POST)
        if form.is_valid():
            warehouse_release = form.save()
            component = Component.objects.get(id=request.POST['component'])
            component.stock_level -= int(request.POST['amount'])
            new_comp = component.save()
            return redirect('/')
        else:
            return render(request, 'warehouse_release.html', {'form': form})


#  jak to działa?
# class WarehouseReleaseFormView(FormView):  # do uzupełnienia
#     template_name = 'warehouse_release.html'
#     form_class = WarehouseReleaseForm
#     success_url = '/'
#
#     def form_valid(self, request):
#         component = Component.objects.get(id=request.POST['component'])
#         component.stock_level -= int(request.POST['amount'])
#         new_comp = component.save()
#         return super(WarehouseReleaseFormView, self).form_valid(form)


class StockLevelView(View):
    def get(self, request):
        components = Component.objects.all()
        return render(request, 'stock_level.html', {'components': components})
