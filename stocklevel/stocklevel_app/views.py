from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from .models import Component, Supplier, Product, Recipient, WarehouseFlows

from .forms import ComponentForm, ProductForm, SupplierForm, RecipientForm, WarehouseEntryForm,\
    WarehouseReleaseForm, WarehouseEntryLaboratoryForm, LoginForm


class BaseView(View):

    """starting view"""

    def get(self, request):
        return render(request, 'base.html')


class ComponentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):

    """view with a form to create new component"""

    model = Component
    fields = ['name', 'measure']
    success_url = '/components/'


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):

    """view with a form to create new product"""

    model = Product
    fields = '__all__'
    success_url = '/'


class RecipientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):

    """view with a form to create new recipient"""

    model = Recipient
    fields = '__all__'
    success_url = '/'


class SupplierCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):

    """view with a form to create new supplier"""

    model = Supplier
    fields = '__all__'
    success_url = '/suppliers/'


class ComponentsView(View):

    """view to show list of all components"""

    def get(self, request):
        components = Component.objects.all()
        return render(request, 'components.html', {'components': components})


class ComponentView(View):

    """view to show details of chosen component"""

    def get(self, request, component_id):
        component = Component.objects.get(id=component_id)
        return render(request, 'component.html', {'component': component})


class SuppliersView(View):

    """view to show list of all suppliers"""

    def get(self, request):
        suppliers = Supplier.objects.all()
        return render(request, 'suppliers.html', {'suppliers': suppliers})


class SupplierView(View):

    """view to show details of chosen supplier"""

    def get(self, request, supplier_id):
        supplier = Supplier.objects.get(id=supplier_id)
        components = supplier.component.all()
        return render(request, 'supplier.html', {'supplier': supplier, 'components': components})


class WarehouseEntryCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):

    """view to enter a new delivery of component do warehouse"""

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
class WarehouseReleaseView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):

    """View to release component from warehouse to the laboratory, production or removal"""

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


class AddLaboratoryNumberView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):

    """View to add laboratory number after internal laboratory investigation"""

    model = WarehouseFlows
    form_class = WarehouseEntryLaboratoryForm
    template_name_suffix = '_update_form'
    success_url = '/stock-level/'


class AllEntriesView(View):

    """View to show list of all entries to the warehouse"""

    def get(self, request):
        entries = WarehouseFlows.objects.all().order_by('delivery_date')
        return render(request, 'all_entries.html', {'entries': entries})


class EntryDetailedView(LoginRequiredMixin, PermissionRequiredMixin, View):

    """View to show details of chosen entry to the warehouse"""

    def get(self, request, entry_id):
        entry = WarehouseFlows.objects.get(id=entry_id)
        return render(request, 'detailed_entry.html', {'entry': entry})


class StockLevelView(View):

    """View to show level of all components in the warehouse"""

    def get(self, request):
        components = Component.objects.all().order_by('name')
        return render(request, 'stock_level.html', {'components': components})


class SupplierUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):

    """View to update information about chosen supplier"""

    model = Supplier
    fields = ['comment', 'category']
    template_name_suffix = '_update_form'
    success_url = '/suppliers/'


class LoginView(View):

    """View to login user"""

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'login.html', {'form': form})
        else:
            return render(request, 'login.html', {'form': form})


class LogoutView(View):

    """View to logout user"""

    def get(self, request):
        logout(request)
        return redirect('/')
