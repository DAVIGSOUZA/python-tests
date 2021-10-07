from django.urls import path
from django.urls.resolvers import URLPattern
from .views import index, contact

urlpatterns = [
    path('', index),
    path('contato', contact)
]