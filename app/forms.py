from dataclasses import field, fields
from pyexpat import model
from tkinter import Widget
from tkinter.tix import Select
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from django.forms import ModelForm, TextInput

from .models import Customer, Tax, User, Product, Image, Cart, OrderPlaced, Coupon, Color, Size, Supplier


class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 
        'email', 
        'password1', 
        'password2'
        ]
        labels = {'email':'Email'}
        Widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs=
    {"autocomplete": "current-password", 'class':'form-control'}))

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"), 
    strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete': 'current-password', 'autofocus':True,  
    'class':'form-control'}))
    new_password1 = forms.CharField(label=_("New Password"), 
    strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete': 'new-password', 'class':'form-control'}),
    help_text=password_validation.
    password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), 
    strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete': 'new-password', 'class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs=
    {'autocomplete': 'email', 'class':'form-control'}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), 
    strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete': 'new-password', 'class':'form-control'}),
    help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), 
    strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete': 'new-password', 'class':'form-control'}))

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 
        'locality', 
        'city', 
        'zipcode', 
        'state'
        ]
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}), 
                   'locality':forms.TextInput(attrs={'class':'form-control'}), 
                   'city':forms.TextInput(attrs={'class':'form-control'}), 
                   'zipcode':forms.NumberInput(attrs={'class':'form-control'}),
                   'state':forms.Select(attrs={'class':'form-control'})
                }

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['group', 
        'item_type', 
        'manufacturer', 
        'supplier', 
        'title', 
        'barcode', 
        'item_size', 
        'item_color', 
        'actual_mrp', 
        'purchase_price', 
        'selling_price', 
        'discounted_price', 
        'purchase_tax', 
        'selling_tax', 
        'description', 
        'brand', 
        'category', 
        'product_purchase_date', 
        'expiry_date', 
        'product_image'
        ]
        widgets = {
            'group' :forms.TextInput(attrs={'class':'form-control'}),
            'item_type' :forms.TextInput(attrs={'class':'form-control'}), 
            'manufacturer' :forms.TextInput(attrs={'class':'form-control'}), 
            'supplier' :forms.Select(attrs={'class':'form-control'}), 
            'title' :forms.TextInput(attrs={'class':'form-control'}), 
            'barcode' :forms.NumberInput(attrs={'class':'form-control'}), 
            'item_size' :forms.Select(attrs={'class':'form-control'}), 
            'item_color' :forms.Select(attrs={'class':'form-control'}), 
            'purchase_price' :forms.NumberInput(attrs={'class':'form-control'}), 
            'actual_mrp' :forms.NumberInput(attrs={'class':'form-control'}), 
            'selling_price' :forms.NumberInput(attrs={'class':'form-control'}),
            'discounted_price' :forms.NumberInput(attrs={'class':'form-control'}),  
            'purchase_tax' :forms.NumberInput(attrs={'class':'form-control'}), 
            'selling_tax' :forms.NumberInput(attrs={'class':'form-control'}), 
            'description' :forms.TextInput(attrs={'class':'form-control'}), 
            'brand' :forms.TextInput(attrs={'class':'form-control'}), 
            'category' :forms.Select(attrs={'class':'form-control'}), 
            'product_purchase_date' :forms.DateInput(attrs={'class':'form-control'}), 
            'expiry_date' :forms.DateInput(attrs={'class':'form-control'}), 
            'product_image' :forms.ClearableFileInput(attrs={'class':'form-control'}), 
        }

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['mobile_no', 
        'user', 
        'name', 
        'email', 
        'locality', 
        'city', 
        'zipcode', 
        'state'
        ]
        Widgets = {
            'mobile_no' :forms.TextInput(attrs={'class':'form-control'}), 
            'user' :forms.TextInput(attrs={'class':'form-control'}), 
            'name' :forms.TextInput(attrs={'class':'form-control'}), 
            'email' :forms.EmailInput(attrs={'class':'form-control'}), 
            'locality' :forms.TextInput(attrs={'class':'form-control'}), 
            'city' :forms.TextInput(attrs={'class':'form-control'}), 
            'zipcode' :forms.TextInput(attrs={'class':'form-control'}), 
            'state':forms.Select(attrs={'class':'form-control'})
        }

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields =['product', 'pimage']
        widgets = {
            'product' :forms.Select(attrs={'class':'form-control'}), 
            'pimage' :forms.FileInput(attrs={'class':'form-control'})
        }

class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = ['cart_id', 'customer', 'product', 'quantity']
        Widgets = {
            'cart_id' :forms.NumberInput(attrs={'class':'form-control'}),
            'customer' :forms.Select(attrs={'class':'form-control'}),
            'product' :forms.Select(attrs={'class':'form-control'}),
            'quantity' :forms.NumberInput(attrs={'class':'form-control'})
        }

class OrderPlacedForm(ModelForm):
    class Meta:
        model = OrderPlaced
        fields = ['user', 'customer', 'product', 'quantity', 'order_date', 'status']
        widgets = {
            'user' :forms.Select(attrs={'class':'form-control'}), 
            'customer' :forms.Select(attrs={'class':'form-control'}), 
            'product' :forms.Select(attrs={'class':'form-control'}), 
            'quantity' :forms.NumberInput(attrs={'class':'form-control'}), 
            'order_date' :forms.DateInput(attrs={'class':'form-control'}), 
            'status' :forms.Select(attrs={'class':'form-control'})
        }

class CouponForm(ModelForm):
    class Meta:
        model = Coupon
        fields = ['code', 'valid_from', 'valid_to', 'discount', 'active']                                   
        input_type = 'date'                                                                                                                                                                                                                                                                                                                                                                                                                        
        Widgets ={
            'code' :forms.TextInput(attrs={'class':'form-control'}), 
            'valid_from' :forms.DateInput(attrs={'class':'form-control', 'type':'date'}), 
            'valid_to' :forms.DateInput(attrs={'class':'form-control'}), 
            'discount' :forms.NumberInput(attrs={'class':'form-control'}), 
            'active' :forms.CheckboxInput(attrs={'class':'form-control'})
        }

class TaxForm(ModelForm):
    class Meta:
        model = Tax
        fields = ('tax_type', 'value')
        Widgets ={
            'tax_type' :forms.TextInput(attrs={'class':'form-control'}), 
            'value' :forms.NumberInput(attrs={'class':'form-control'})
        }

class ColorForm(ModelForm):
    model = Color
    fields = ('color_code', 'item_color')
    widgets = {
        'color_code' :forms.NumberInput(attrs={'class':'form-control'}), 
        'item_color' :forms.TextInput(attrs={'class':'form-control'})
    }

class SizeForm(ModelForm):
    model = Size
    fields = ('size_code', 'size')
    Widgets = {
        'size_code' :forms.NumberInput(attrs={'class':'form-control'}), 
        'size' :forms.TextInput(attrs={'class':'form-control'})
    }
class SupplierForm(ModelForm):
    model = Supplier
    fields = ['supplier_code', 'supplier', 'address', 'contact_no', 'supplier_email', 'gstin_no', 'state', 'pin']
    widgets = {
        'supplier_code' :forms.NumberInput(attrs={'class':'form-control'}), 
        'supplier' :forms.TextInput(attrs={'class':'form-control'}), 
        'address' :forms.TextInput(attrs={'class':'form-control'}), 
        'contact_no' :forms.NumberInput(attrs={'class':'form-control'}), 
        'supplier_email' :forms.EmailInput(attrs={'class':'form-control'}), 
        'gstin_no' :forms.TextInput(attrs={'class':'form-control'}), 
        'state' :forms.TextInput(attrs={'class':'form-control'}), 
        'pin' :forms.NumberInput(attrs={'class':'form-control'})
    }

# class UserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#         Widgets ={
#             'username' :forms.TextInput(attrs={'class':'form-control'}), 
#             'email' :forms.EmailInput(attrs={'class':'form-control'}), 
#             'password1' :forms.PasswordInput(attrs={'class':'form-control'}), 
#             'password2' :forms.PasswordInput(attrs={'class':'form-control'})
#         }