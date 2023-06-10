from .models import Product
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.forms import UserCreationForm

from .models import User, Product
from django import forms

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter your Username'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter your Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Enter your Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Confirm your password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class MyModelForm(forms.ModelForm):
#     content = forms.CharField(widget=CKEditorWidget())

#     class Meta:
#         model = Product
#         fields = '[descrption,]'


class MyModelAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Product
        fields = '__all__'
        # fields = [
        #     'slug',
        #     'name',
        #     'status',
        #     'trending',
        #     'meta_tilte',
        #     'meta_keyword',
        #     'meta_description',
        #     'create_at',
        #     'update_at',
        #     'category',
        #     'small_descrption',
        #     'quantity',
        #     'original_price',
        #     'selling_price',
        #     'tags'
        # ]


# 'slug',
# 'name',
# 'status',
# 'trending',
# 'meta_tilte',
# 'meta_keyword',
# 'meta_description',
# 'create_at',
# 'update_at',
# 'category',
# 'small_descrption',
# 'quantity',
# 'original_price',
# 'selling_price',
# 'tags'
