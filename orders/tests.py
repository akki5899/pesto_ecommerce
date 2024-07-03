from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from .models import Order
from products.models import Product

User = get_user_model()

class OrderTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.force_authenticate(user=self.user)
        self.product = Product.objects.create(name='Test Product', description='A test product', price='10.00', stock=100)
        self.order_data = {
            'product': self.product.id,
            'quantity': 1
        }

    def test_create_order(self):
        response = self.client.post('/api/orders/', self.order_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().user, self.user)

    def test_list_orders(self):
        Order.objects.create(user=self.user, product=self.product, quantity=1)
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
