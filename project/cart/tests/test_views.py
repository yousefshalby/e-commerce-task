from django.test import TestCase, Client
from django.urls import reverse
from django.core import urlresolvers
from model_mommy import mommy


class Testviews(TestCase):
    def setUp(self):
        self.client = Client()
        self.product=mommy.make('shop.Product')

def test_detail_view(self):
        url =self.client.post(reverse('cart:cart_detail'))    
       
        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed(url, 'cart/detail.html')    


def test_cart_add_view(self):
        url =self.client.post(reverse('cart:cart_add', args=[self.product.id]))

        self.assertEqual(url.status_code, 200)
        self.assertRedirects(url, urlresolvers.reverse('cart:cart_detail'))


def test_cart_remove_view(self):
        url =self.client.post(reverse('cart:cart_remove', args=[self.product.id]))

        self.assertEqual(url.status_code, 200)
        self.assertRedirects(url, urlresolvers.reverse('cart:cart_detail'))

      