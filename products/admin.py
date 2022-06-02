from django.contrib import admin

from products.models import Products, Categoria, Cliente

# Register your models here.
admin.site.register(Products)
admin.site.register(Categoria)
admin.site.register(Cliente)