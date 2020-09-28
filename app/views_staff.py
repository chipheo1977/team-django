from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required #??
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from datetime import datetime
from .models import *

def index(request):
    return render(request, 'index.html')

def listCategory(request):
    listCate = Category.objects.all()
    return render(request, 'category/index.html', {'listCate': listCate})

def addCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-category')
        
    return render(request, 'category/add.html', {'form': form})

def updateCategory(request, pk):
    category = Category.objects.get(pk=pk)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST ,instance=category)
        if form.is_valid():
            form.save()
            return redirect('list-category')
    return render(request, 'category/edit.html', {'form': form})

def deleteCategory(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('list-category')

# PHẦN SẢN PHẨM

def listProduct(request):
    products = Product.objects.all()
    return render(request, 'product/index.html', {'products': products})

def addProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list-product')
    return render(request, 'product/add.html', {'form': form})

def updateProduct(request, pk):
    p = Product.objects.get(pk=pk)
    form = ProductForm(instance=p)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=p)
        if form.is_valid():
            form.save()
            return redirect('list-product')
    return render(request, 'product/edit.html', {'form': form})

def deleteProduct(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('list-product')






def demo(request):
    return render(request, 'base.html')