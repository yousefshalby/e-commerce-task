from django.http import request
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, resolve
from orders.models import OrderItem
from cart.cart import Cart
from django.conf import settings
from model_mommy import mommy
from orders.forms import OrderCreateForm
from importlib import import_module

class Testviews(TestCase):
    def setUp(self):
        self.client = Client()
        self.orderitem = mommy.make('orders.OrderItem', quantity=4, price=5)
        self.orderitem = OrderCreateForm(data={
            'first_name':'ali',
            'last_name':'omar',
            'email':'ali@example.com',
            'address':'mahoud st',
            'postal_code': 2255,
            'city': 'alex'
        })

        request.session['order']={
            'first_name':'ali',
            'last_name':'omar',
            'email':'ali@example.com',
            'address':'mahoud st',
            'postal_code': 2255,
            'city': 'alex'
        }
        request.session.save()

    def test_cart_post_request(self):

        request =self.client.post(reverse('orders:order_create'),data={'item' :self.orderitem})
        request.session['new']=request.data
        request.session.save()
        self.response = Cart(request)

        self.assertEqual(self.response.status_code, 201)


    def test_cart_get_request(self): 
        request = self.client.get(reverse('orders:order_create'))
        request.session.get('order')
        response = Cart(request)

        self.assertEqual(response.status_code, 200)


    def test_create_view(self):
        url =self.client.get(reverse('orders:order_create'))

        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed( url, 'orders/order/create.html')



    def test_CreateOrder_context(self):
        response = self.client.get(reverse('orders:order_create'))
        
        self.assertIsInstance(response.context['form'], OrderCreateForm)
