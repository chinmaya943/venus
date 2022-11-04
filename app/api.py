import json
from datetime import datetime
# from rest_framework import permissions
# from rest_framework import routers, serializers, viewsets, generics
# from django_filters.rest_framework import DjangoFilterBackend

from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.shortcuts import render
from .models import Cart, Customer, Product, Tax, Coupon


# class ProductSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'

# class ProductListAPIView(viewsets.ModelViewSet):
# serializer_class = ProductSerializer
# queryset = Product.objects.all()
# model = serializer_class.Meta.model
# filter_backends = [DjangoFilterBackend]
# permission_classes = [permissions.IsAuthenticated]

# def get_queryset(self):
#     barcode = self.kwargs.get('barcode')
#     print(self.kwargs)
#     queryset = self.model.objects.filter(barcode=barcode)
#     return queryset

# router = routers.DefaultRouter()
# router.register('product', ProductListAPIView, basename='Product')


def filter_product(request):
    if request.method != 'POST':
        return JsonResponse({
            'error': 'Method not Allowed',
            'status_code': 405
        }, status=405)

    barcode = request.POST.get('barcode')
    products = Product.objects.filter(barcode__icontains=barcode)

    data = {'data': list(products.values())}
    return JsonResponse(data)


def filter_customer(request):
    if request.method != 'POST':
        return JsonResponse({
            'error': 'Method not Allowed',
            'status_code': 405
        }, status=405)

    phone = request.POST.get('phone')
    customer = Customer.objects.filter(mobile_no__icontains=phone)

    data = {'data': list(customer.values())}
    return JsonResponse(data)


def save_bill(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('data', '{}'))
        customer = Customer.objects.filter(
            mobile_no=data.get('phone', '')).first()
        if customer is None:
            customer = Customer(mobile_no=data.get(
                'phone'), name=data.get('name'), email=data.get('email'))
            customer.save()

        now = datetime.now()
        coupon = Coupon.objects.filter(
            code=data.get('coupon_code'),
            active=True,
            valid_from__lte=now,
            valid_to__gt=now
        ).first()
        now = now.strftime('%y%m%d%H%M%S')
        cart_id = f'{customer.mobile_no}_{now}'

        cart_items = []
        products = data.get('products', [])
        for product in products:
            barcode = product['barcode']
            product_obj = Product.objects.filter(barcode=barcode).first()
            cart = Cart(cart_id=cart_id, customer=customer,
                        product=product_obj,
                        quantity=product.get('quantity', 1),
                        offer_applied=coupon)
            cart_items.append(cart)

        carts = Cart.objects.bulk_create(cart_items)
        return JsonResponse({'cart_id': cart_id})

    if request.method == 'GET':
        cart_id = request.GET.get('data', '')
        cart_items = Cart.objects.filter(cart_id=cart_id)
        customer = {}
        if len(cart_items):
            customer['name'] = cart_items[0].customer.name
            customer['phone'] = cart_items[0].customer.mobile_no
            customer['email'] = cart_items[0].customer.email

        products = []
        for item in cart_items:
            product = serializers.serialize('json', [item.product])
            product = json.loads(product)[0].get('fields')
            product['quantity'] = item.quantity
            products.append(product)

        out = {
            'cart_id': cart_id,
            'customer': customer,
            'products': products
        }
        if cart_items and cart_items[0].offer_applied:
            coupon = cart_items[0].offer_applied
            out['coupon'] = {
                'code': coupon.code,
                'discount': coupon.discount
            }

        return JsonResponse(out)

    return JsonResponse({
        'error': 'Method not Allowed',
        'status_code': 405
    }, status=405)


def taxes(request):
    return JsonResponse({'taxes': list(Tax.objects.all().values())})


def check_coupon(request):
    if request.method == 'GET':
        now = datetime.now()
        coupon = Coupon.objects.filter(
            code=request.GET.get('code'),
            active=True,
            valid_from__lte=now,
            valid_to__gt=now
        ).first()

        if coupon:
            return JsonResponse(
                {'valid': True, 
            'code': coupon.code, 
            'discount': coupon.discount
            }
            )
        else:
            return JsonResponse({'valid': False})
    
    return JsonResponse({
        'error': 'Method not Allowed',
        'status_code': 405
    }, status=405)