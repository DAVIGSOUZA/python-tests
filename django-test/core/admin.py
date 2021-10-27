from django.contrib import admin

from .models import Product, Client


# mostrar colunas da model em admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'storage')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


# necessário registrar a ClasseAdmin junto a model apropriada para mostrar na área de admin
admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
