from itertools import product
from pyclbr import Function
import re
from tkinter import Button
from typing import List
from unicodedata import category
from django import views
from django.shortcuts import redirect, render,HttpResponsePermanentRedirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.views import View
from .models import CASHIER, MANAGER,ACCOUNTANT,  STAFF_CATEGORY_CHOICES, Color, Coupon, Customer, Product, Cart, OrderPlaced, Coupon, Size, Supplier, Tax
from .forms import CartForm, ColorForm, SizeForm, SupplierForm, CouponForm, CustomerRegistrationForm, CustomerProfileForm, OrderPlacedForm, ProductForm, CustomerForm, TaxForm    
from django.db.models import Q
from django.http import JsonResponse
# For Function based login view
from django.contrib.auth.decorators import login_required
# For Class based login view
from django.utils.decorators import method_decorator
from django.contrib.auth import views as auth_views
from .models import Product, Cart, Customer, OrderPlaced, User
from django.template import RequestContext
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError



def home(request):
    # view = ProductView()
    # return view.get(request)
    return redirect('login')
# Admin Views

class CustomLoginView(auth_views.LoginView):
    template_name = 'app/login.html'
    success_url = '/dologin'

#login page
def login(request):
    if request.user.is_superuser:
        return redirect('admin-home')
    elif request.user.staff_category == MANAGER:
        return render(request, 'staff/staff_home.html')
    elif request.user.staff_category == CASHIER:
        return render(request, 'cash_counter/cashier_home.html')
    elif request.user.staff_category == ACCOUNTANT:
        return render(request, 'accountant_app/accountant_home.html')
    else:
        return redirect('home')

def dashboard(request):
    return render(request, 'admin_app/admin_home.html')

# Staff view
def staff_dashboard(request):
    return render(request, 'staff/staff_home.html')

# Cashier view
def cashier_dashboard(request):
    return render(request, 'cash_counter/cashier_home.html')


# Product View list(Admin)
def all_products(request):
    product_list = Product.objects.all()
    return render(request, 'admin_app/products.html', {'product_list':product_list})

# Product Delete(admin)
def delete_data(request, id):
    if request.method =='POST':
        pd=Product.objects.get(pk=id)
        pd.delete()
        return HttpResponseRedirect('admin_app/products.html')

# product Update(admin)
def update_data(request, id):
    if request.method == 'POST':
        pu = Product.objects.get(pk=id)
        fm = ProductForm(request.POST, instance=pu)
        if fm.is_valid():
            fm.save()
            fm.clean()
    else:
        pu = Product.objects.get(pk=id)
        fm = ProductForm(instance=pu)
    return render(request, 'admin_app/update_product.html', {'form':fm})

# Product View list(Staff)
def all_product(request):
    products_list = Product.objects.all()
    return render(request, 'staff/products.html', {'products_list':products_list})

# Product View list(cashier)
def all_productss(request):
    productss_list = Product.objects.all()
    return render(request, 'cash_counter/products.html', {'productss_list':productss_list})

# Cart View list(Admin)
def all_carts(request):
    cart_list = Cart.objects.all()
    return render(request, 'admin_app/carts.html', {'cart_list':cart_list})

# Cart Delete(admin)
def cart_delete(request, id):
    if request.method =='POST':
        cd=Cart.objects.get(pk=id)
        cd.delete()
        return HttpResponseRedirect('admin_app/carts.html')

# Cart View list(Staff)
def all_cart(request):
    carts_list = Cart.objects.all()
    return render(request, 'staff/carts.html', {'carts_list':carts_list})

# Customer View list(Admin)
def all_customer(request):
    customer_list = Customer.objects.all()
    return render(request, 'admin_app/customers.html', {'customer_list':customer_list})

# Customer Delete(admin)
def customer_delete(request, id):
    if request.method =='POST':
        cd=Customer.objects.get(pk=id)
        cd.delete()
        return HttpResponseRedirect('admin_app/customers.html')

# Customer Update(admin)
def update_cust(request, id):
    if request.method == 'POST':
        cu = Customer.objects.get(pk=id)
        fm = CustomerForm(request.POST, instance=cu)
        if fm.is_valid():
            fm.save()
            fm.clean()
    else:
        cu = Customer.objects.get(pk=id)
        fm = CustomerForm(instance=cu)
    return render(request, 'admin_app/update_customer.html', {'form':fm})


# Customer View list(Staff)
def all_customeres(request):
    customers_list = Customer.objects.all()
    return render(request, 'staff/customers.html', {'customers_list':customers_list})


# Order-Placed list(Admin)
def all_orderplaced(request):
    orderplaced_list = OrderPlaced.objects.all()
    return render(request, 'admin_app/order_placed.html', {'orderplaced_list':orderplaced_list})

# Order_Placed Delete(admin)
def op_delete(request, id):
    if request.method =='POST':
        cd=OrderPlaced.objects.get(pk=id)
        cd.delete()
        return HttpResponseRedirect('admin_app/order_placed.html')

# Order_Placed Update(admin)
def op_update(request, id):
    if request.method == 'POST':
        opu = OrderPlaced.objects.get(pk=id)
        fm = OrderPlacedForm(request.POST, instance=opu)
        if fm.is_valid():
            fm.save()
            fm.clean()
    else:
        opu = OrderPlaced.objects.get(pk=id)
        fm = OrderPlacedForm(instance=opu)
    return render(request, 'admin_app/update_order_place.html', {'form':fm})

# Order-Placed list(Staff)
def all_orderplace(request):
    orderplace_list = OrderPlaced.objects.all()
    return render(request, 'staff/order_placed.html', {'orderplace_list':orderplace_list})

# Users list(Admin)
def all_users(request):
    users_list = User.objects.all()
    # print(users_list)
    return render(request, 'admin_app/users.html', {'users_list':users_list})

# Users insert
def user_insert(request):
    submitted = False
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user_insert?submitted=True')
    else:
        form = CustomerRegistrationForm
        if 'submitted' in request.GET:
            submitted =True
    return render(request, 'admin_app/userinsertform.html', {'form':form, 'submitted':submitted})

# Users Delete(admin)
def u_delete(request, id):
    if request.method =='POST':
        cd=User.objects.get(pk=id)
        cd.delete()
        return HttpResponseRedirect('admin_app/users.html')

# Users list(Staff)
def all_user(request):
    user_list = User.objects.all()
    # print(user_list)
    return render(request, 'staff/users.html', {'user_list':user_list})

# Coupon List
def all_coupon(request):
    coupon_list = Coupon.objects.all()
    return render(request, 'admin_app/coupon.html', {'coupon_list':coupon_list})

# Coupon Update(admin)
def coupon_update(request, id):
    if request.method == 'POST':
        cou = Coupon.objects.get(pk=id)
        fm = CouponForm(request.POST, instance=cou)
        if fm.is_valid():
            fm.save()
            fm.clean()
    else:
        cou = Coupon.objects.get(pk=id)
        fm = CouponForm(instance=cou)
    return render(request, 'admin_app/update_coupon.html', {'form':fm})

# Coupon Delete(admin)
def c_delete(request, id):
    if request.method =='POST':
        cd=Coupon.objects.get(pk=id)
        cd.delete()
        return HttpResponseRedirect('admin_app/coupon.html')

# Tax list(admin)
def all_tax(request):
    tax_list = Tax.objects.all()
    return render(request, 'admin_app/tax.html', {'tax_list':tax_list})

# Tax delete(delete)
def tax_delete(request, id):
    if request.method =='POST':
        tx = Tax.objects.get(pk=id)
        tx.delete()
        return render(request, 'admin_app/tax.html')

# Tax Update(admin)
def update_tax(request, id):
    if request.method == 'POST':
        tu = Tax.objects.get(pk=id)
        fm = TaxForm(request.POST, instance=tu)
        if fm.is_valid():
            fm.save()
            fm.clean()
    else:
        tu = Tax.objects.get(pk=id)
        fm = TaxForm(instance=tu)
    return render(request, 'admin_app/update_tax.html', {'form':fm})

# Color list(admin)
def all_color(request):
    color_list = Color.objects.all()
    return render(request, 'admin_app/color.html', {'color_list':color_list})

# Size list(admin)
def all_size(request):
    size_list = Size.objects.all()
    return render(request, 'admin_app/size.html', {'size_list':size_list})

# Supplier list(admin)
def all_supplier(request):
    supplier_list = Supplier.objects.all()
    return render(request, 'admin_app/supplier.html', {'supplier_list':supplier_list})

# Supplier Delete(admin)
def supplier_delete(request, id):
    if request.method =='POST':
        cd=Supplier.objects.get(pk=id)
        cd.delete()
        return HttpResponseRedirect('admin_app/supplier.html')

# Supplier Update(admin)
def supplier_update(request, id):
    if request.method == 'POST':
        opu = Supplier.objects.get(pk=id)
        fm = SupplierForm(request.POST, instance=opu)
        if fm.is_valid():
            fm.save()
            fm.clean()
    else:
        opu = Supplier.objects.get(pk=id)
        fm = SupplierForm(instance=opu)
    return render(request, 'admin_app/update_supplier.html', {'form':fm})

# Bill-page
def bill_page(request):
    return render(request, 'bills.html')

# Product insert(Admin)
def productinsert(request):
    submitted = False
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(productinsert)
    else:
        form = ProductForm()
        if 'submitted' in request.GET:    
            submitted = True
    return render(request, 'admin_app/productinsertform.html', {'form':form, 'submitted':submitted})

# Product insert(Staff)
def product_insert(request):
    submitted = False
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(productinsert)
    else:
        form = ProductForm()
        if 'submitted' in request.GET:    
            submitted = True
    return render(request, 'staff/productinsertform.html', {'form':form, 'submitted':submitted})

# Customer insert
def customerinsert(request):
    if not request.user.is_superuser:
        return redirect(request.META.get('HTTP_REFERER', '/'))
    submitted = False
    if request.method  == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(customerinsert)
    else:
        form = CustomerForm()
        if 'subnitted' in request.GET:
            submitted = True
    return render(request, 'admin_app/customerinsertform.html', {'form':form, 'submitted':submitted})

# Cart insert
def cartinsert(request):
    submitted = False
    if request.method == "POST":
        form = CartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(cartinsert)
    else:
        form = CartForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'admin_app/cartinsertform.html', {'form':form, 'submitted':submitted})

# Orderplaced insert
def order_placed(request):
    submitted = False
    if request.method == "POST":
        form = OrderPlacedForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/order_olaced?submitted=True')
    else:
        form = OrderPlacedForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'admin_app/opinsert.html', {'form':form, 'submitted':submitted})



# # User Update(Admin)
# def update_users(request, id):
#     if request.method == 'POST':
#         uu = User.objects.get(pk=id)
#         fm = 

# Coupon insert
def coupon_insert(request):
    submitted = False
    if request.method == 'POST':
        form = CouponForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/coupon_insert?submitted=True')
    else:
        form = CouponForm()
        if 'submitted' in request.GET:
            submitted = True 
    return render(request, 'admin_app/coupon_insert.html', {'form':form, 'submitted':submitted})

# Tax insert
def tax_insert(request):
    submitted = False
    if request.method == 'POST':
        form = TaxForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tax_insert?submitted=True')
    else:
        form = TaxForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'admin_app/tax_insert.html', {'form':form, 'submitted':submitted})

# color insert
def color_insert(request):
    submitted = False
    if request.method == 'POST':
        form = ColorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/color_insert?submitted=True')
    else:
        form = ColorForm()
        if 'submitted' in request.GET:
            submitted = True
            return render(request, 'admin_app/color_insert.html', {'form':form, 'submitted':submitted}) 

# color delete
def color_delete(request, id):
    if request.method =='POST':
        tx = Color.objects.get(pk=id)
        tx.delete()
        return render(request, 'admin_app/color.html')

# Supplier insert
def supplier_insert(request):
    submitted = False
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(supplier_insert)
    else:
        form = SupplierForm()
        if 'submitted' in request.GET:
            submitted = True
            return render(request, 'admin_app/supplier_insert.html', {'form':form, 'submitted':submitted})

    # Size Insert
def sizevalue_insert(request):
    submitted = False
    if request.method == 'POST':
        form = SizeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('admin_app/size-insert?submitted=True')
    else:
        form = SizeForm()
        if 'submitted' in request.GET:
            submitted = True
            return render(request, 'admin_app/size_insert.html', {'form':form, 'submitted':submitted})



# size delete
def size_delete(request, id):
    if request.method =='POST':
        tx = Size.objects.get(pk=id)
        tx.delete()
        return render(request, 'admin_app/size.html')

# Coupon Update(admin)
def update_coupon(request,id):
    if request.method == 'POST':
        co = Coupon.objects.get(pk=id)
        fm = CouponForm(request.POST, instance=co)
        if fm.is_valid():
            fm.save()
            fm.clean()
    else:
        co = Coupon.objects.get(pk=id)
        fm = CouponForm(instance=co)
    return render(request, 'admin_app/update_coupon.html', {'form':fm})


# Update product
def update_product(request):
    product = Product.objects.get()
    return render(request, 'admin_app/update_product.html', {'product':product})

# User Views
#Home/Product view
class ProductView(View):
    def get(self, request):
        KitchenSteelproduct = Product.objects.filter(category='Kitchen Steelproduct')
        Grocery = Product.objects.filter(category='Grocery')
        Vegitables = Product.objects.filter(category='Vegitables')
        FreshFruits = Product.objects.filter(category='Fresh Fruits')
        Snacks = Product.objects.filter(category='Snacks')
        ColdDrinks = Product.objects.filter(category='Cold Drinks')
        DryfruitsNuts = Product.objects.filter(category='Dryfruits & Nuts')
        HotDrinks = Product.objects.filter(category='Hot Drinks') 
        Protins = Product.objects.filter(category='Protins')
        BeautyProducts = Product.objects.filter(category='Beauty Products')
        OtherHomeProdects = Product.objects.filter(category='Other Home Products')
        return render(request, 'app/home.html', {'KitchenSteelproduct':KitchenSteelproduct, 'Grocery':Grocery, 'Vegitables':Vegitables, 'FreshFruits':FreshFruits, 'Snacks':Snacks, 'ColdDrinks':ColdDrinks, 'DryfruitsNuts':DryfruitsNuts, 'HotDrinks':HotDrinks, 'Protins':Protins, 'BeautyProducts':BeautyProducts, 'OtherHomeProdects':OtherHomeProdects})

# product details
class ProductDetailsView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(Q(product=product) & Q(customer__user=request.user)).exists()
        return render(request, 'app/productdetail.html', {'product':product, 'item_already_in_cart':item_already_in_cart}) 

# search Function
def searchbar(request):
    if request.method =='GET':
        search = request.GET.get('search')
        prod = Product.objects.all().filter(title=search)
        return render(request, 'app/searchbar.html', {'prod':prod})

#add to cart
@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')

#view cart
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        # print(cart)

        #calculation/no product in cart
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.customer == user]
        # print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
                totalamount = amount + shipping_amount
            return render(request, 'app/addtocart.html', {'carts':cart, 'totalamount':totalamount, 'amount':amount})
        else:
            return render(request, 'app/emptycart.html')
            
# Plus cart quantity & amount
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        # print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.customer == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount


        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount + shipping_amount
            }
        return JsonResponse(data)

# Minus cart quantity & amount
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        # print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.customer == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': amount + shipping_amount

            }
        return JsonResponse(data)

#  Minus cart quantity & amount
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        # print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.customer == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'amount': amount,
            'totalamount': amount + shipping_amount
            }
        return JsonResponse(data)

#buy now function
def buy_now(request):
    return render(request, 'app/buynow.html')

#address view
@login_required
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html', {'add':add, 'active':'btn-primary'})

# Orders
@login_required
def orders(request):
    op = OrderPlaced.objects.filter(user=request.user)
    return render(request, 'app/orders.html', {'order_placed':op})

#procuct view
#mobile Cold Drinks
# def mobile(request, data=None):
#     mobiles = []
#     if data == None:
#         mobiles = Product.objects.filter(category='M')
#     elif data == 'Redmi' or data == 'Samsung' or data == 'Iphone' or data == 'Vivo' or data == 'Oppo':
#         mobiles = Product.objects.filter(category='M').filter(brand=data)
#     elif data =='Below':
#         mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=10000)
#     elif data =='Above':
#         mobiles = Product.objects.filter(category='M').filter(discounted_price__gt=10000)
#     return render(request, 'app/mobile.html', {'mobiles':mobiles})


def admin_home(request):
    return render(request, 'admin_app/admin_home.html')

def staff_home(request):
    return render(request, 'staff/staff_home.html')

def cashier_home(request):
    return render(request, 'cash_counter/cashier_home.html')

#registration page
class CustomerRegistrationFormView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form':form})
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations..! Registered Successfully')
        return render(request, 'app/customerregistration.html', {'form':form})    

#checkout page
@login_required
def checkout(request):
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 70.0
    totalamount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.customer == request.user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
        totalamount = amount + shipping_amount
    return render(request, 'app/checkout.html', {'add':add, 'totalamount':totalamount, 'cart_items':cart_items})

@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity).save()
        c.delete()
    return redirect("orders")

# user profile page
@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=user, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Congratulations..!! ProfileUpdated Successfully.')
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})


def exit_bill(request):
    return render(request, 'app/home.html')

def bill_print(request):
    return render(request, 'bill_print.html')
