from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product, Category
from django.contrib.auth.models import User

class ProductModelTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category = Category.objects.create(name="Electronics", description="Electronic Items")
        self.product = Product.objects.create(
            name="Laptop",
            description="A powerful laptop",
            unit="pcs",
            unitPrice=1000.00,
            quantityInStock=50,
            category=self.category
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Laptop")
        self.assertEqual(self.product.category.name, "Electronics")

    def test_product_list_authentication(self):
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CategoryModelTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.category = Category.objects.create(name="Electronics", description="Electronic Items")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Electronics")

    def test_category_list_authentication(self):
        response = self.client.get(reverse('category-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('category-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
