from re import template
from django.conf import settings
from django.urls import include, path, reverse
from app import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
from django.views.generic import RedirectView
from django.contrib import admin
from . import api



urlpatterns = [
    
    path('', views.home, name="home"),
    path('dologin/', views.login, name='dologin'),
    path('searchbar', views.searchbar, name='searchbar'),
    path('product\\-detail/<int:pk>', views.ProductDetailsView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart), 
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),

    path('account/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),   
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'), 
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
    
    path('registration/', views.CustomerRegistrationFormView.as_view(), name='customerregistration'),

    # for admin
    path('admin-home/', views.admin_home, name="admin-home"),
    path('dashboard', views.dashboard, name="dashboard"), 

    path('products', views.all_products, name="list-products"),
    path('delete/<int:id>/', views.delete_data, name='deletedata'),
    path('<int:id>/', views.update_data, name='update_data'),

    path('carts', views.all_carts, name="list-carts"),
    path('deletes/<int:id>/', views.cart_delete, name="deletesdata"),  

    path('customers', views.all_customer, name="list-customers"),
    path('cudelete/<int:id>/', views.customer_delete, name="customer-delete"), 
    path('update/<int:id>/', views.update_cust, name= "customer-update"), 


    path('order-placed', views.all_orderplaced, name="list-order_placed"),
    path('opdelete/<int:id>/', views.op_delete, name="op-delete"), 
    path('opupdate/<int:id>/', views.op_update, name='op-update'), 

    path('users', views.all_users, name="list-users"),
    path('udelete/<int:id>/', views.u_delete, name="u-delete"),
    path('user_update/<int:id>/', views.update_cust, name="user-update"),  

    path('coupons', views.all_coupon, name="list-coupons"),
    path('coupondelete/<int:id>/', views.c_delete, name="coupon-delete"), 
    path('updatecoup/<int:id>/', views.update_coupon, name="coupon-update"),

    path('taxes', views.all_tax, name="list-tax"),
    path('taxdelete/<int:id>', views.tax_delete, name="tax-delete"),
    path('updatetax<int:id>/', views.update_tax, name="update-tax"),    

    path('colors', views.all_color, name="list-color"), 
    path('colordelete/<int:id>', views.color_delete, name="color-delete"), 

    path('sizes', views.all_size, name="list-size"),
    path('sizedalate/<int:id>', views.size_delete, name="size-delete"),  

    path('supplier', views.all_supplier, name="list-supplier"),
    path('supplierdelete/<int:id>/', views.supplier_delete, name="supplier-delete"), 
    path('supplierupdate/<int:id>/', views.supplier_update, name='supplier-update'), 


    path('bills', views.bill_page, name="list-bills"),
    path('add-product', views.productinsert, name="P-insert"),
    path('add-customer', views.customerinsert, name="Cu-insert"),
    path('add-cart', views.cartinsert, name="Ca-insert"),
    # path('add-order_placed', views.order_placed, name="Op-insert"),
    path('add-users', views.user_insert, name="U-insert"),
    path('add-coupon', views.coupon_insert, name="co-insert"),
    path('add-tax', views.tax_insert, name="tax-insert"),
    path('add-color', views.color_insert, name="color-insert"),
    path('add-supplier', views.supplier_insert, name="supplier-insert"),
    path('add-size', views.sizevalue_insert, name="size-insert"), 
    
    

    # path('update_product', views.update_product, name='update-product'),

    # for staff
    path('staff-home/', views.staff_home, name= "staff-home"),
    path('staff_dashboard', views.staff_dashboard, name="staff_dashboard"),
    path('product', views.all_product, name="lists-products"),
    path('add-products', views.product_insert, name="Product-insert"),
    path('cartss', views.all_cart, name="lists-carts"),
    path('customer', views.all_customeres, name="list-customeress"),
    path('order-place', views.all_orderplace, name="list-order_place"),
    path('user', views.all_user, name="list-user"),
    path('bills', views.bill_page, name="list-bills"),

    # for cashier
    path('cashier-home/', views.cashier_home, name="cashier-home"),
    path('productss', views.all_productss, name="list-productss"),
    path('bills', views.bill_page, name="list-bills"),

    path('exit', views.exit_bill, name='exit_bill'),
    
    path('demo', views.bill_print, name="demo"), 


    # path('api/', include(router.urls)),
    path('api/product', api.filter_product),
    path('api/customer', api.filter_customer),
    path('api/bill', api.save_bill),
    path('api/taxes', api.taxes),
    path('api/check_coupon', api.check_coupon),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
