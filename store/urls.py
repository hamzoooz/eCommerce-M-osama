from django.urls import path, include
from . import views
from store.controler import authview, card, wishlist, checkout, order

urlpatterns = [
    # path('ckeditor/', include('ckeditor.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', views.index, name='index'),
    path('collections/', views.collections, name='collections'),
    path('collections/<str:slug>', views.collectionsview, name='collectionsview'),
    path('collections/<str:cat_slug>/<str:prod_slug> ', views.productview, name='productview'),

    path('procced-list/', views.productlist, name='productlist'),
    path('searchproduct', views.searchproduct, name='searchproduct'),

    path('register/', authview.register, name='register'),
    path('login/', authview.loginPage, name='login'),
    path('logout/', authview.logoutPage, name='logout'),

    path('add-to-card', card.addtocard, name='addtocard'),
    path('card', card.cardview, name='card'),
    path('update-card', card.updatecard, name='updatecard'),
    path('delete_card_item', card.delete_card_item, name='delete_card_item'),
    
    
    
    
    path('wishlist', wishlist.index, name='wishlist'),
    path('add-to-wishlist', wishlist.addwishlist, name='addtowishlist'),
    path('delete-to-wishlist', wishlist.deletewishlistiteme, name='deletewishlistiteme'),
    
    
    
    path('checkout', checkout.checkout, name='checkout'),
    path('placeorder', checkout.placeorder, name='placeorder'),
    path('procced_to_pay', checkout.razrppaychick , name='procced_to_pay'),

    path('my-orders', order.orders, name='my_order'),
    path('orderview/<t_no>', order.orderview, name='orderview'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

]
# urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
