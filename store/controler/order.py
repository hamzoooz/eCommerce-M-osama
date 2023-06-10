from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from store.models import Order, OrderItem

@login_required(login_url='login')
def orders(request):
    order = Order.objects.filter(user=request.user)
    context = {"order":order}
    return render(request, 'store/order/order.html', context)



def orderview(request, t_no):
    order = Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitem  = OrderItem.objects.filter(order=order)
    context = {"order": order,"orderitem":orderitem }
    
    return render(request, "store/order/view.html",context)

