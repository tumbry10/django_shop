from django.db import models
from accounts.models import CustomUser


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='brand_logos', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'brand'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    description = models.TextField(blank=True, null=True)
    size = models.CharField(max_length=10, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name


class StockIn(models.Model):
    received_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    date_received = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'stock_in'

    def __str__(self):
        return f"StockIn #{self.id} on {self.date_received.strftime('%Y-%m-%d')}"


class StockInItem(models.Model):
    stock_in = models.ForeignKey(StockIn, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_received = models.PositiveIntegerField()

    class Meta:
        db_table = 'stock_in_item'

    def __str__(self):
        return f"{self.quantity_received} x {self.product.name}"


class Sale(models.Model):
    sold_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    date_sold = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        db_table = 'sale'


    def __str__(self):
        return f"Sale #{self.id} on {self.date_sold.strftime('%Y-%m-%d')}"


class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_sold = models.PositiveIntegerField()
    price_at_sale = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'sale_item'

    def __str__(self):
        return f"{self.quantity_sold} x {self.product.name} @ {self.price_at_sale}"
