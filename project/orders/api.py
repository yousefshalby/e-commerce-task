from rest_framework import viewsets
from rest_framework.response import Response
from orders.models import Order
from orders.serializers import  OrderSerializer
from rest_framework import status, filters



class ViewSet_order(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer 
    filter_backend = [filters.SearchFilter]       
    search_fields = ['first_name', 'last_name']