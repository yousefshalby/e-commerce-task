from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from orders.models import Order
from orders.api import ViewSet_order

class OrderSerializerTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.payload = {
           'first_name':'ali',
            'last_name':'omar',
            'email':'ali@example.com',
            'address':'mahoud st',
            'postal_code': 2255,
            'city': 'alex'
        }
    def test_Order_creation(self):

        response = self.client.post(reverse("orders:order_list"), self.payload)
        self.assertEqual(self.status.HTTP_201_CREATED, response.status_code)      

    
    def test_view_set(self):
        request = self.client.get("")
        cat_detail = ViewSet_order.as_view({'get': 'retrieve'})
        order = Order.objects.create(first_name="bob")
        response = cat_detail(request, pk=order.pk)
        self.assertEqual(response.status_code, 200)