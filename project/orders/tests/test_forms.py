# from django.test import TestCase
# from orders.forms import OrderCreateForm

# class TestForms(TestCase):  
#     def test_orders_valid_data(self):
#         form = OrderCreateForm(data={
#             'first_name':'ali',
#             'last_name':'omar',
#             'email':'ali@example.com',
#             'address':'mahoud st',
#             'postal_code': 2255,
#             'city': 'alex'
#         })


#         self.assertTrue(form.is_valid())  


#     def test_orders_with_no_data(self):
#         form = OrderCreateForm(data={})

#         self.assertFalse(form.is_valid())
#         self.assertEqual(len(form.errors), 6)            