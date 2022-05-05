from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='ShopHome'),
    path("about/", views.about, name='About'),
    path("contact/", views.contact, name='Contact'),
    path("search", views.search, name='Search'),
    path("cart/", views.cart, name='Cart'),
    path("track", views.track, name='track'),
    path("productView/<int:prod_id>", views.productView, name='productView'),
]
