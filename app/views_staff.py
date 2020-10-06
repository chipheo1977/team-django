from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required #??
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from datetime import datetime
from .forms import *
from .models import *

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def listCategory(request):
    listCate = Category.objects.all()
    return render(request, 'category/index.html', {'listCate': listCate})

@login_required
def addCategory(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-category')
        
    return render(request, 'category/add.html', {'form': form})

@login_required
def updateCategory(request, pk):
    category = Category.objects.get(pk=pk)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST ,instance=category)
        if form.is_valid():
            form.save()
            return redirect('list-category')
    return render(request, 'category/edit.html', {'form': form})

@login_required
def deleteCategory(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('list-category')

# PHẦN SẢN PHẨM

@login_required
def listProduct(request):
    products = Product.objects.all()
    return render(request, 'product/index.html', {'products': products})

@login_required
def addProduct(request):
    ImagesProductFormSet = modelformset_factory(ImagesProduct, form=ImagesProductForm, extra=3)
    if request.method == 'POST':
        productForm = ProductForm(request.POST)
        formset = ImagesProductFormSet(request.POST, request.FILES, queryset=ImagesProduct.objects.none())
        
        if productForm.is_valid() and formset.is_valid():
            product_form = productForm.save(commit=False)
            product_form.save()

            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = ImagesProduct(product=product_form, image=image)
                    photo.save()
                    
            messages.success(request, "Yeeew, check it out on the home page!")
            return redirect('list-product')
        else:
            print(productForm.errors, formset.errors)
            print(formset)
    else:
        productForm = ProductForm()
        formset = ImagesProductFormSet(queryset=ImagesProduct.objects.none())
    return render(request, 'product/add.html', {'productForm': productForm, 'formset': formset})

@login_required
def detailProduct(request, pk):
    p = Product.objects.get(pk=pk)
    imgP = ImagesProduct.objects.all()
    return render(request, 'product/detail.html', {'p': p, 'imgP': imgP})

@login_required
def updateProduct(request, pk):
    p = Product.objects.get(pk=pk)
    form = ProductForm(instance=p)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=p)
        if form.is_valid():
            form.save()
            return redirect('list-product')
    return render(request, 'product/edit.html', {'form': form})

@login_required
def deleteProduct(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('list-product')

def get_current_path(request):
    return render(request, 'base.html', {'current_path': request.get_full_path()})




def demo(request):
    return render(request, 'base.html')