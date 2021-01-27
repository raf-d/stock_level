import django.forms as forms
from .models import Component, Recipient, Supplier, Product, WarehouseEntry, WarehouseRelease


class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = '__all__'


class RecipientForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = '__all__'


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class WarehouseEntryForm(forms.ModelForm):
    class Meta:
        model = WarehouseEntry
        exclude = ['delivery_date']


class WarehouseReleaseForm(forms.ModelForm):
    class Meta:
        model = WarehouseRelease
        fields = '__all__'  # zmienić jeżeli data ma wypełniać się automatycznie
