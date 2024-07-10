from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="Default description")

    def __str__(self):
        return self.name

    def get_products(self):
        return self.products.all()

    def addProduct(self, product):
        product.category = self
        product.save()

    def removeProduct(self, product):
        if product.category == self:
            product.category = None
            product.save()

    def findProduct(self, product_id):
        return self.products.filter(id=product_id).first()


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="No description provided")

    def __str__(self):
        return self.name

    def get_products(self):
        return self.products.all()

    def addProduct(self, product):
        product.category = self
        product.save()

    def removeProduct(self, product):
        if product.category == self:
            product.category = None
            product.save()

    def findProduct(self, product_id):
        return self.products.filter(id=product_id).first()


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    unit = models.CharField(max_length=50, default="units")
    unitPrice = models.DecimalField(max_digits=10, decimal_places=2)
    quantityInStock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

    def restock(self, amount):
        self.quantityInStock += amount
        self.save()

    def updatePrice(self, new_price):
        self.unitPrice = new_price
        self.save()
