from django.urls import path
from . import views

urlpatterns = [
    path('addCart', views.add_to_cart, name='add_to_cart'),
    path('viewCart', views.view_cart, name='view_cart'),
    path('removeCart', views.remove_from_cart, name='remove_from_cart'),
]
