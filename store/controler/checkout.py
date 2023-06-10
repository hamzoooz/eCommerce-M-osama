from django.http import JsonResponse , HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from store.models import Product, Card, Order, OrderItem, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

import random


@login_required(login_url='login')
def checkout(request):
    rawCard = Card.objects.filter(user=request.user)
    for item in rawCard:
        # print(item.product.quantity)
        if item.product_qty > item.product.quantity:
            Card.objects.delete(id=item.id)
    carditem = Card.objects.filter(user=request.user)

    total_pricing = 0
    for item in carditem:
        total_pricing = total_pricing + item.product.selling_price * item.product_qty

    user_profile = Profile.objects.filter(user=request.user).first()
    
    context = {"carditem": carditem, 'total_pricing': total_pricing, "user_profile":user_profile}

    return render(request, 'store/checkout/checkout.html', context)


@login_required(login_url='login')
def placeorder(request):
    if request.method == "POST":

        current_user = User.objects.filter(id=request.user.id).first()

        if not current_user.first_name:
            current_user.first_name = request.POST.get('fname')
            current_user.last_name = request.POST.get('lname')
            current_user.save()

        if not Profile.objects.filter(user=request.user):
            user_profile = Profile()
            user_profile.user = request.user
            user_profile.phone = request.POST.get('phone')
            user_profile.address = request.POST.get('address')
            user_profile.city = request.POST.get('city')
            user_profile.stats = request.POST.get('stats')
            user_profile.conutry = request.POST.get('conutry')
            user_profile.pincode = request.POST.get('pincode')
            user_profile.save()

        new_order = Order()

        new_order.user = request.user
        new_order.fname = request.POST.get('fname')
        new_order.lname = request.POST.get('lname')
        new_order.email = request.POST.get('email')
        new_order.phone = request.POST.get('phone')
        new_order.address = request.POST.get('address')
        new_order.city = request.POST.get('city')
        new_order.stats = request.POST.get('stats')
        new_order.conutry = request.POST.get('conutry')
        new_order.pincode = request.POST.get('pincode')

        new_order.payment_mode = request.POST.get('payment_mode')
        new_order.payment_id = request.POST.get('payment_id')

        card = Card.objects.filter(user=request.user)
        card_total_price = 0
        for item in card:
            card_total_price = card_total_price + \
                item.product.selling_price * item.product_qty

        new_order.total_price = card_total_price
        trackno = "hamzoooz" + str(random.randint(1111111, 9999999))
        while Order.objects.filter(tracking_no=trackno) is None:
            trackno = "hamzoooz" + str(random.randint(1111111, 9999999))
        new_order.tracking_no = trackno

        new_order.save()

        new_order_item = Card.objects.filter(user=request.user)
        for item in new_order_item:
            OrderItem.objects.create(
                order=new_order,
                quantity=item.product_qty,
                price=item.product.selling_price,
                product=item.product,
            )

            order_product = Product.objects.filter(id=item.product_id).first()
            order_product.quantity = order_product.quantity - item.product_qty
            order_product.save()

        # To Clear User's Card
        Card.objects.filter(user=request    .user).delete()
        
        messages.success(request, 'Your Order has been placed successfuly ! ')

        payMode = request.POST.get('payment_mode')
        if ( payMode == "Paid by Razorpay" ):
            
            return JsonResponse( { 'status': 'Your Order has been placed successfuly ! '}  )

    # else:
    return redirect('index')
    
    # return render(request, 'store/checkout/placeholder.html')


@login_required(login_url='login')
def razrppaychick(request):
    card = Card.objects.filter(user=request.user)
    total_price = 0 
    for item in card :
        total_price = total_price + item.product.selling_price * item.product_qty
    return JsonResponse({'total_price': total_price})

# def orders(request):
#     return HttpResponse('My Order Page ')
    # JsonResponse('status':"successfuly")
# name, create_at, user, product, product_qty

# Product(*, slug, name, descrption, status, trending, meta_tilte, meta_keyword,
# meta_description, create_at, update_at, category, small_descrption, quantity,
# original_price, selling_price, tags)