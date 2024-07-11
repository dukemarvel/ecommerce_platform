from django.test import TestCase
from .models import Product, Category

class ProductModelTest(TestCase):

    def setUp(self):
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

class CategoryModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Electronics", description="Electronic Items")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Electronics")
