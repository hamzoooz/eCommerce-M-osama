from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from store.models import Product, Card
from django.contrib.auth.decorators import login_required


def addtocard(request):
    if request.method == 'POST':
        print(request.POST)
        if request.user.is_authenticated:
            # prod_id = request.POST.get('product_id')
            # product_name = request.POST.get('product_name')
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if (product_check):
                if (Card.objects.filter(user=request.user.id, product_id=prod_id)):
                    return JsonResponse({'status':'Product Alrady in Card'})
                else:
                    prod_qty = int(request.POST.get('product_qty'))
                    products_name = request.POST.get('products_name')
                    if product_check.quantity >= prod_id :
                        Card.objects.create(
                            user=request.user, product_id=prod_id, product_qty=prod_qty, name=products_name)
                        return JsonResponse({'status':'Product Added successfully'})
                    else:
                        return JsonResponse({'status':'Only' + str(product_check.quantity) + "quantity available" })
            else:
                return JsonResponse({'status':'No Such Product Found '})
        else:
            return JsonResponse({'status':'Login To Continue'})

    return redirect('index')

@login_required(login_url="login")
def cardview(request):
    if request.user.is_authenticated:
        card = Card.objects.filter(user=request.user)
        context = { 'card':card }
        return render(request, 'store/card/card.html', context )
    else:
        return redirect('login')

    
# @login_required(login_url="login")
def updatecard(request):
    if request.method == "POST":
        prod_id = int(request.POST.get('product_id'))
        if (Card.objects.filter(user=request.user, product_id=prod_id)):
            prod_qty = int(request.POST.get("product_qty"))
            card = Card.objects.get(product_id=prod_id, user=request.user)
            card.product_qty = prod_qty
            card.save()
            return JsonResponse({"status": "Updae Successfully"})
        return redirect('index')


# @login_required(login_url="login")
def delete_card_item(request):
    if request.method == "POST":
        prod_id = int(request.POST.get('product_id'))
        print(prod_id)
        if (Card.objects.filter(user=request.user, product_id=prod_id)):
            carditem = Card.objects.get(product_id=prod_id, user=request.user)
            carditem.delete()
        return JsonResponse({'status':'Delete Successfuly'})
    return redirect('index')