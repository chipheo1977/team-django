from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name','slug', 'status')

class ProductForm(forms.ModelForm):
    #image = forms.ImageField(widget=forms.FileInput(attrs={'multiple': ''}))
    #name = forms.CharField(max_length=128)
    
    class Meta:
        model = Product
        fields = '__all__'

class ImagesProductForm(forms.ModelForm):
    image = forms.ImageField(label='ảnh chi tiết')
    #main_image = forms.ImageField(label='ảnh chính')
    class Meta:
        model = ImagesProduct
        fields = ('image',)

class SomeForm(forms.Form):
    text = forms.CharField(widget = forms.Textarea(attr={'class':'richtexteditor'})