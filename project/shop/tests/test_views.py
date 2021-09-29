from django.test import TestCase, Client
from django.urls import reverse, resolve
from shop.models import Category, Product


class Testviews(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category()
        self.category.name = 'robot'
        self.category.slug = 'hello-world'
        self.category.save()

        self.product =Product()
        self.product.name='cars'
        self.product.slug='cell-phones'
        self.product.description='i am good'
        self.product.price='20.0'
        self.product.category = Category()
        self.product.category.save()
        self.product.save()
        


    def test_product_list_view(self):
        url =self.client.get(reverse('shop:product_list'))

        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed( url, 'shop/product/list.html')

    def test_category_exist(self):
        self.assertTrue(Category.objects.all().count() > 0)
        


    def test_get_category_with_specefic_slug(self):
        res = self.client.get(self.category.get_absolute_url())
        
        self.assertContains(res, self.category.name)
        self.assertContains(res, self.category.slug)


    def test_404_category(self):   
        res = self.client.get(reverse('shop:product_list_by_category', args=['money']))
        self.assertEqual(res.status_code, 404)  



    def test_product_detail_view(self):
        url =self.client.get(reverse('shop:product_detail',args=[self.product.id, self.product.slug]))

        self.assertEqual(url.status_code, 200)
        self.assertTemplateUsed( url, 'shop/product/detail.html')

  
    def test_get_specific_products_(self):  #Reverse for 'product_list_by_category' with arguments '('',)'not found
        res = self.client.get(self.product.get_absolute_url())
        
        self.assertContains(res, self.product.name)
        self.assertContains(res, self.product.description)
        self.assertEqual(res.status_code, 200)


    def test_404_product(self):   
        res = self.client.get(reverse('shop:product_detail', args=[ 3, 'money']))
        self.assertEqual(res.status_code, 404)