from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
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
    fields = ['name', 'measure']
    success_url = '/'