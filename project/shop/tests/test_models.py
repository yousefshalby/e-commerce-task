# from django.test import TestCase
# from shop.models import Category, Product

# class categoryTest(TestCase):
#     def setUp(self):
#         self.category = Category()
#         self.category.name = "make more tests"
#         self.category.slug = "become-better-at-testing"
#         self.category.save()

#     def test_str_is_equal_to_name(self):
#         record = Category.objects.get(pk=self.category.id)
#         self.assertEqual(str(record), self.category.name)


#     def test_get_absolute_url(self):
#         self.assertEquals(self.category.get_absolute_url(), "/%s/" %(self.category.slug))


# class productTest(TestCase):
#     def setUp(self):
#         self.product = Product()
#         self.product.name = "make more tests"
#         self.product.slug = "become-better-at-testing"
#         self.product.price = '10'
#         self.product.category = Category()
#         self.product.category.save()
#         self.product.save()

#     def test_str_is_equal_to_name(self):
#         record = Product.objects.get(pk= self.product.id)
#         self.assertEqual(str(record), self.product.name)


#     def test_get_absolute_url_product(self):
#         self.assertEqual(self.product.get_absolute_url(), "/%s/%s/" %(self.product.id, self.product.slug))        