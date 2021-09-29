from django.urls import path, include
from . import views
from . import api
from orders.api import *
from rest_framework.routers import DefaultRouter

app_name = 'orders'

router = DefaultRouter()
router.register('orderslist', api.ViewSet_order)

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('rest/viewsets/', include(router.urls)),
]
