from django.db import models


# Category model
class Category(models.Model):
  name = models.CharField(max_length=100, unique=True)
  
  def __str__(self):
    return self.name

# product model 
class Product(models.Model):
  name = models.CharField(max_length=100)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
  description = models.TextField(blank=True, null=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.name

# stock model
class Stock(models.Model):
  product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='stock')
  quantity = models.PositiveIntegerField()
  updated_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
     return f"{self.product.name} - {self.quantity} pcs"