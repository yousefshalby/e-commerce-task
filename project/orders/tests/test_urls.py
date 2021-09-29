from django.test import TestCase,Client, RequestFactory
from django.urls import reverse, resolve
from orders.models  import Order
from orders.views import order_create

class Testurls(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()


    def test_create_order(self):
        url = self.client.get(reverse('orders:order_create')) 
        response = resolve(reverse('orders:order_create'))
        
        self.assertEquals(url.status_code, 200)
        self.assertEquals(response.func, order_create)
    