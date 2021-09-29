from django.test import TestCase
from orders.models import Order, OrderItem
from model_mommy import mommy


class OrderTest(TestCase):
    def setUp (self):
        self.order = mommy.make('orders.Order')
        self.orderitem = mommy.make('orders.OrderItem', quantity=3, price=2, _quantity=2)   
      
    def test_is_str_equal_to_id(self):      
        record = Order.objects.get(pk=self.order.id)
        self.assertEqual(str(record), 'Order '+str(self.order.id))   
        
    def test_total_cost(self):
        self.assertEqual(sum(item.get_cost() for item in self.orderitem), 12.00)


class OrderItemTest(TestCase):
    def setUp (self):
        self.orderitem = mommy.make('orders.OrderItem', quantity=2, price=3)

    def test_is_str_equal_to_id(self):      
        record = OrderItem.objects.get(pk=self.orderitem.id)
        self.assertEqual(str(record), str(self.orderitem.id))

    def test_get_cost(self): 
        self.assertEqual(self.orderitem.price * self.orderitem.quantity, 6)            