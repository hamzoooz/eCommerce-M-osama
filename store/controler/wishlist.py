from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from store.models import Product, Card,Wishlist
from django.contrib.auth.decorators import login_required
# ss Wishlist(*, create_at, user, product

@login_required(login_url='login')
def index(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    context = {'wishlist': wishlist, }
    return render(request, 'store/wishlist.html', context)


def addwishlist(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            print(prod_id)
            product_check = Product.objects.filter(id=prod_id)
            if (product_check):
                if (Wishlist.objects.filter(user=request.user, product_id=prod_id)):
                    return JsonResponse({'status':'Prodduct Alrady in Wishlist'})
                else:
                    Wishlist.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({'status':'Prodduct Added To Wishlist Successfuly ! '})
            else:
                return JsonResponse({"status":"No Such Product Found"})
        else:
            return JsonResponse({"status":"Login To Continue"})
    return redirect('index')


def deletewishlistiteme(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            print(prod_id)
            if (Wishlist.objects.filter(user=request.user, product_id=prod_id)):
                wishlistitem = Wishlist.objects.get(product_id=prod_id)
                wishlistitem.delete()
                return JsonResponse({'status': 'Wishlist Delete Successfuly !'})
            else:
                return JsonResponse({"status":"Product Not Found in Wishkist"})
        else:
            return JsonResponse({"status":"Login To Continue "})
    return redirect('index')

