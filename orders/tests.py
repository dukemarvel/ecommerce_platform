from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Cart, CartItem, Order, OrderItem
from products.models import Product, Category
from django.contrib.auth.models import User

class OrderModelTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        self.category = Category.objects.create(name="Electronics", description="Electronic Items")
        self.product = Product.objects.create(
            name="Laptop",
            description="A powerful laptop",
            unit="pcs",
            unitPrice=1000.00,
            quantityInStock=50,
            category=self.category
        )
        self.cart = Cart.objects.create(user=self.user)
        self.cart_item = CartItem.objects.create(cart=self.cart, product=self.product, quantity=1)
        self.order = Order.objects.create(user=self.user, total=1000.00)
        self.order_item = OrderItem.objects.create(order=self.order, product=self.product, quantity=1)

    def test_order_creation(self):
        self.assertEqual(self.order.user.username, 'testuser')
        self.assertEqual(self.order_item.product.name, 'Laptop')

    def test_order_list(self):
        response = self.client.get(reverse('order-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_cart_creation(self):
        self.assertEqual(self.cart.user.username, 'testuser')
        self.assertEqual(self.cart_item.product.name, 'Laptop')

    def test_cart_list(self):
        response = self.client.get(reverse('cart-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
