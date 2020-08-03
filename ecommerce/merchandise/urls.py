from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.merchandise, name="merchandise"), 
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('image_view/', views.imageView, name="image_view"),
    path('login_page/', views.loginPage, name="login_page")
    
]
