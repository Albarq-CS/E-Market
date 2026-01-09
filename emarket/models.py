from django.db import models

class Category(models.Model):
    catName = models.CharField(max_length=100)
    def __str__(self):
        return self.catName

class Supplier(models.Model):
    suppName = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)

    def __str__(self):
        return self.suppName

class Product(models.Model):
    prodName = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Suppliers = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.prodName
