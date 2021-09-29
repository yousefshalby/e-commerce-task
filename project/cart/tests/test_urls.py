from django.test import TestCase,Client, RequestFactory
from django.urls import reverse, resolve
from cart.views import cart_add, cart_detail, cart_remove
from shop.models import Product
from model_mommy import mommy

class Testurls(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.product=mommy.make('shop.Product')

    # def test_cart_detail(self):
    #     url = self.client.get(reverse('cart:cart_detail')) 
    #     response = resolve(reverse('cart:cart_detail'))
        
    #     self.assertEquals(url.status_code, 200)
    #     self.assertEquals(response.func, cart_detail)

    # def test_cart_add(self):
    #     request =self.factory.post('cart/cart_add/')
    #     response = cart_add(request, product_id=self.product.id)
    #     url = resolve(reverse('cart:cart_add', args=[self.product.id]))


    #     self.assertEquals(200, response.status_code)
    #     self.assertEquals(url.func, cart_add)    

    # def test_cart_remove(self):
    #     request =self.client.get('cart/cart_remove/')
    #     response = cart_remove(request, product_id=self.product.id)
    #     #url = resolve(reverse('cart:cart_remove', args=[self.product.id]))


    #     self.assertEquals(200, response.status_code)
    #     #self.assertEquals(url.func, cart_remove)        