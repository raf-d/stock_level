import django.forms as forms
from .models import Component, Recipient, Supplier, Product, WarehouseFlows


class DateInput(forms.DateInput):
    input_type = 'date'


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
        widgets = {
            'component': forms.CheckboxSelectMultiple()
        }
        # nie działa


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'production_start': DateInput(attrs={'type': 'date'}),
            'production_finish': DateInput(attrs={'type': 'date'})
        }


class WarehouseEntryForm(forms.ModelForm):
    class Meta:
        model = WarehouseFlows
        exclude = ['laboratory_series_number', 'laboratory_series_date', 'release_date',
                   'release_purpose', 'release_amount']
        widgets = {
            'use_by_date': DateInput(attrs={'type': 'date'}),
            'delivery_date': DateInput(attrs={'type': 'date'})
        }


class WarehouseReleaseForm(forms.ModelForm):
    class Meta:
        model = WarehouseFlows
        fields = ['component', 'series_amount', 'release_date', 'release_purpose', 'release_amount']
        widgets = {
            'release_date': DateInput(attrs={'type': 'date'}),
            'component': forms.HiddenInput,
            'series_amount': forms.HiddenInput
        }

    # dodane do weryfikacji ilości materiału
    def clean(self):
        cleaned_data = self.cleaned_data
        series_amount = cleaned_data['series_amount']
        release_amount = cleaned_data['release_amount']

        if release_amount > series_amount:
            raise forms.ValidationError('Nie ma tyle materiału na stanie')


class WarehouseEntryLaboratoryForm(forms.ModelForm):
    class Meta:
        model = WarehouseFlows
        fields = ['laboratory_series_number', 'laboratory_series_date']
        widgets = {
            'laboratory_series_date': DateInput(attrs={'type': 'date'}),
        }


class LoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
