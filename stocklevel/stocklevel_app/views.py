from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from .models import Component, Supplier, Product, Recipient, WarehouseFlows
from .forms import WarehouseEntryForm, WarehouseReleaseForm, WarehouseEntryLaboratoryForm, LoginForm, ProductForm


class BaseView(View):

    """starting view"""

    def get(self, request):
        return render(request, 'base.html')


class ComponentCreateView(PermissionRequiredMixin, CreateView):

    """view with a form to create new component"""

    permission_required = ('stocklevel_app.add_component')
    model = Component
    fields = ['name', 'measure']
    success_url = '/components/'


class ProductCreateView(PermissionRequiredMixin, CreateView):

    """view with a form to create new product"""

    permission_required = ('stocklevel_app.add_product')
    model = Product
    form_class = ProductForm
    success_url = '/products/'


class RecipientCreateView(PermissionRequiredMixin, CreateView):

    """view with a form to create new recipient"""

    permission_required = ('stocklevel_app.add_recipient')
    model = Recipient
    fields = '__all__'
    success_url = '/recipients/'


class SupplierCreateView(PermissionRequiredMixin, CreateView):

    """view with a form to create new supplier"""

    permission_required = ('stocklevel_app.add_supplier')
    model = Supplier
    fields = '__all__'
    success_url = '/suppliers/'


class ComponentsView(LoginRequiredMixin, View):

    """view to show list of all components"""

    def get(self, request):
        components = Component.objects.all()
        return render(request, 'components.html', {'components': components})


class ComponentView(LoginRequiredMixin, View):

    """view to show details of chosen component"""

    def get(self, request, component_id):
        component = Component.objects.get(id=component_id)
        return render(request, 'component.html', {'component': component})


class SuppliersView(LoginRequiredMixin, View):

    """view to show list of all suppliers"""

    def get(self, request):
        suppliers = Supplier.objects.all()
        return render(request, 'suppliers.html', {'suppliers': suppliers})


class SupplierView(LoginRequiredMixin, View):

    """view to show details of chosen supplier"""

    def get(self, request, supplier_id):
        supplier = Supplier.objects.get(id=supplier_id)
        components = supplier.component.all()
        return render(request, 'supplier.html', {'supplier': supplier, 'components': components})


class ProductsView(LoginRequiredMixin, View):

    """view to show list of all products"""

    def get(self, request):
        products = Product.objects.all()
        return render(request, 'products.html', {'products': products})


class ProductView(LoginRequiredMixin, View):

    """view to show details of chosen product"""

    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        return render(request, 'product.html', {'product': product})


class RecipientsView(LoginRequiredMixin, View):

    """view to show list of all recipients"""

    def get(self, request):
        recipients = Recipient.objects.all()
        return render(request, 'recipients.html', {'recipients': recipients})


class WarehouseEntryCreate(PermissionRequiredMixin, CreateView):

    """view to enter a new delivery of component do warehouse"""

    permission_required = ('stocklevel_app.add_warehouseflows')
    form_class = WarehouseEntryForm
    model = WarehouseFlows
    success_url = '/stock-level/'

    def form_valid(self, form):
        new_entry = form.save()
        component = form.cleaned_data['component']
        component.stock_level += int(form.cleaned_data['series_amount'])
        new_comp = component.save()
        return redirect('/stock-level/')


class WarehouseReleaseView(PermissionRequiredMixin, UpdateView):

    """View to release component from warehouse to the laboratory, production or removal"""

    permission_required = ('stocklevel_app.change_warehouseflows')
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


class AddLaboratoryNumberView(PermissionRequiredMixin, UpdateView):

    """View to add laboratory number after internal laboratory investigation"""

    permission_required = ('stocklevel_app.change_warehouseflows')
    model = WarehouseFlows
    form_class = WarehouseEntryLaboratoryForm
    template_name_suffix = '_update_form'
    success_url = '/stock-level/'


class AllEntriesView(LoginRequiredMixin, View):

    """View to show list of all entries to the warehouse"""

    def get(self, request):
        entries = WarehouseFlows.objects.all().order_by('delivery_date')
        return render(request, 'all_entries.html', {'entries': entries})


class EntryDetailedView(LoginRequiredMixin, View):

    """View to show details of chosen entry to the warehouse"""

    def get(self, request, entry_id):
        entry = WarehouseFlows.objects.get(id=entry_id)
        return render(request, 'detailed_entry.html', {'entry': entry})


class StockLevelView(View):

    """View to show level of all components in the warehouse"""

    def get(self, request):
        components = Component.objects.all().order_by('name')
        return render(request, 'stock_level.html', {'components': components})


class SupplierUpdate(PermissionRequiredMixin, UpdateView):

    """View to update information about chosen supplier"""

    permission_required = 'stocklevel_app.change_supplier'
    model = Supplier
    fields = ['comment', 'category']
    template_name_suffix = '_update_form'
    success_url = '/suppliers/'


class ProductUpdate(PermissionRequiredMixin, UpdateView):

    """View to update information about chosen supplier"""

    permission_required = 'stocklevel_app.change_product'
    model = Product
    fields = ['production_start', 'production_finish']
    template_name_suffix = '_update_form'
    success_url = '/products/'


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
