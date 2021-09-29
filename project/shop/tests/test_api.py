# from rest_framework.test import APITestCase
# from rest_framework.test import APIClient
# from shop.models import Category, Product
# from django.urls import reverse
# from model_mommy import mommy

# class TestCategory(APITestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.data = {
#             'name':'cell phones',
#             'slug':'cell-phones',
#         }

#         self.category_url = reverse('shop:product_list_by_category_api', args=['cell-phones'])

#     def test_category_by_slug(self):
#         res = self.client.get(self.category_url, self.data)

#         self.assertEqual(self.status.HTTP_201_CREATED, res.status_code)      
    #    self.assertEqual(res.context['name'], self.data['name'])
    #     self.assertEqual(res.data['slug'], self.data['slug'])
    #     self.assertEqual(res.status_code, 200)

    # def test_category_exist(self):
    #     self.assertTrue(Category.objects.all().count() > 0)

    # def test_category_404_slug_exsist(self):
    #     res = self.client.get(self.category_url)
    #     self.assertEqual(res.status_code, 404)


# #class TestProduct(APITestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.product = mommy.make("shop.Product")
#         self.product_data = {
#             'name':'cars',
#             'slug':'hello-world',    
#             'description':'i am good',
#             'price':'20.0'
#         }
#         self.product_url= reverse('shop:product_list_api')
#         self.product_url_by_category = reverse('shop:product_list_by_category_api', args=['hello-world'])
#         self.product_detail_url = reverse('shop:product_detail_api', args=[self.product_data.slug, 'hello-world'])

#     def test_Product_creation(self):
#         res =self.client.get(self.product_url, self.product_data)
#         self.assertEqual(self.status.HTTP_201_CREATED, res.status_code)      

#     def test_products_exists(self):  
#          self.assertEqual(Product.objects.all().count() > 0)
        

#     def test_product_list(self): 
#         res =self.client.get(self.product_url, self.product_data)
        
#         self.assertContains(res, self.product_data.name)
#         self.assertContains(res, self.product_data.price)


#     def test_product_by_slug(self):
#         res = self.client.get(self.product_url_by_category, self.product_data)
        
#         self.assertEqual(res.data['name'], self.data['name'])
#         self.assertEqual(res.data['description'], self.data['description'])
#         self.assertEqual(res.status_code, 200)



#     def test_category_404_slug_exsist(self):
#         res = self.client.get(self.category_url)
#         self.assertEqual(res.status_code, 404)


#     def test_product_detail(self):
#         res =self.client.get(self.product_detail_url, self.product_data)

#         self.assertContains(res, self.product_data.name)
#         self.assertContains(res, self.product_data.description)
#         self.assertEqual(res.status_code, 200)
