from django.urls import path
from django.urls.resolvers import URLPattern
from .views import index, contact, product

urlpatterns = [
    path('', index, name='home'),
    path('contato', contact, name='contact'),
    path('produto/<int:pk>', product, name='product')
]