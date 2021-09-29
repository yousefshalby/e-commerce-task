from django.urls import path
from . import views
from . import api
from shop.api import *

app_name = 'shop'

urlpatterns = [
    path('latest-products/', api.LatestProductsList.as_view(), name='product_list_api'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('products/<slug:category_slug>/', api.CategoryDetail.as_view(), name='product_list_by_category_api'),
    path('products/<slug:category_slug>/<slug:product_slug>/', api.ProductDetail.as_view(), name='product_detail_api'),
    path('fav/<int:id>/', views.favourite_add, name='favourite_add'),
    path('profile/favourites/', views.favourite_list, name='favourite_list'),
    path('', views.product_list, name='product_list'),

]
