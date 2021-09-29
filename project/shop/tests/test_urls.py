from shop.models import Category, Product
from django.test import TestCase,Client, RequestFactory
from django.urls import reverse, resolve
from shop.views import  product_list, product_detail
from model_mommy import  mommy


class Testurls(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.product = Product()
        self.product.name = "car"
        self.product.slug = "cars"
        self.product.price = '10'
        self.product.category = Category()
        self.product.category.save()
        self.product.save()
    

#     def test_product_list_url_resolved (self):
#         url = self.client.get(reverse('shop:product_list')) 
#         response = resolve('/')
        
#         self.assertEquals(url.status_code, 200)
#         self.assertEquals(response.func, product_list)

#     def test_product_list_url_category_resolved (self):
#         request =self.factory.get('/shop/product_list_by_category/')
#         response = product_list(request)
#         url = resolve(reverse('shop:product_list_by_category', args=['some-slug']))


#         self.assertEquals(200, response.status_code)
#         self.assertEquals(url.func, product_list)

    # def test_product_detail_url (self, id=1, slug="cars"):
    #     # product = Product.objects.create(name="car", slug= "cars", description="hello world", price=10, category=Category().save())
    #     # product.save()
    #     #product = mommy.make('shop.Product', slug="cars")
    #     request =self.client.get(f'/{id}/{slug}/', self.product)
    #     response = product_detail(request, id=self.product.id, slug=self.product.slug)
    #    # url = resolve(reverse('shop:product_detail', args=[1, 'cars'])) 
       
    #     #self.assertEquals(url.func, product_detail)
    #     self.assertEquals(200, response.status_code)

