from django.contrib import admin
from .models import Component, Recipient, Supplier, Product, WarehouseFlows

# Register your models here.
admin.site.register(Component)
admin.site.register(Recipient)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(WarehouseFlows)
