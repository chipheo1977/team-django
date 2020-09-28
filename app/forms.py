from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name','slug', 'status')

class ProductForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'multiple': ''}))
    class Meta:
        model = Product
        fields = '__all__'