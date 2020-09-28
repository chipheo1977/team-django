from django.urls import path
from .views_staff import *
from django.urls import include

urlpatterns = [
    path('staff', index, name='staff'),
    path('staff/category/', listCategory, name='list-category'),
    path('staff/category/add', addCategory, name='add-category'),
    path('staff/category/update/<pk>', updateCategory, name='update-category'),
    path('staff/category/delete/<pk>', deleteCategory, name='delete-category'),

    path('staff/product/', listProduct, name='list-product'),
    path('staff/product/add', addProduct, name='add-product'), 
    path('staff/product/update/<pk>', updateProduct, name='update-product'),
    path('staff/product/delete/<pk>', deleteProduct, name='delete-product'),

    path('demo', demo, name='demo'),
]