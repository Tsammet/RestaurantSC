from django.urls import path
from . import views

urlpatterns = [
    path('createCategory', views.createCategory, name='createCategory'),
    path('showCategories', views.showCategories, name='showCategories'),
    path('deleteCategory', views.deleteCategory, name='deleteCategory'),
    path('updateCategory', views.updateCategory, name='updateCategory'),
]
