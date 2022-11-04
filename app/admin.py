from django.contrib import admin
from .models import (
    Color,
    Size,
    # Prodgroup,  
    Supplier,  
    Customer,
    Product,
    Cart,
    OrderPlaced,
    User,
    Image,
    Coupon,
    Tax,

)
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


# Register your models here.
@admin.register(User)
class UserModelAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'staff_category']
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (_("Staff Category"), {"fields": ("staff_category",)}),
    )

@admin.register(Color)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['id', 
    'color_code', 
    'item_color'
    ]

@admin.register(Size)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 
    'size_code', 
    'item_size'
    ]

# @admin.register(Prodgroup)
# class ProdgroupModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'p_group_code', 'p_group_name', 'p_group_description']

@admin.register(Supplier)
class SupplierModelAdmin(admin.ModelAdmin):
    list_display = ['id', 
    'supplier_code', 
    'supplier', 
    'address', 
    'contact_no', 
    'supplier_email', 
    'gstin_no', 
    'state', 
    'pin'
    ]

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 
    'mobile_no', 
    'user', 
    'name', 
    'email', 
    'locality', 
    'city', 
    'zipcode', 
    'state'
    ]

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id',
    'group', 
    'item_type', 
    'supplier', 
    'manufacturer', 
    'title', 
    'barcode', 
    'item_size', 
    'item_color', 
    'purchase_price', 
    'purchase_tax', 
    'selling_price', 
    'selling_tax', 
    'discounted_price', 
    'description', 
    'brand', 
    'category', 
    'actual_mrp', 
    'product_purchase_date', 
    'expiry_date', 
    'product_image'
    ]

@admin.register(Image)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ['id', 
    'product', 
    'pimage'
    ]

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 
    'customer', 
    'product', 
    'quantity'
    ]

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 
    'user', 
    'customer', 
    'product', 
    'quantity', 
    'order_date', 
    'status'
    ]

@admin.register(Coupon)
class CouponModelAdmin(admin.ModelAdmin):
    list_display = ['code', 
    'valid_from', 
    'valid_to', 
    'discount', 
    'active'
    ]
    list_filter = ['active', 
    'valid_from', 
    'valid_to'
    ]
    search_fields = ['code']

@admin.register(Tax)
class TaxModelAdmin(admin.ModelAdmin):
    list_display = ['id', 
    'tax_type', 
    'value'
    ]



