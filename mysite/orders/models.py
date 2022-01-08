from django.db import models

from products.models import Product
from customers.models import CustomUser


class Order(models.Model):
    customer_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=100, default='Size', choices=(
        ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('3XL', '3XL'), ('4XL', '4XL')),
                                       blank=True, null=True)  # blank va null
    quantity = models.PositiveIntegerField()
    pay_type = models.CharField(max_length=10, choices=(('click', 'click'), ('payme', 'payme'), ('cash', 'cash')),
                                default='cash')
    address = models.TextField()

    def __str__(self):
        return f"{self.customer_id} - {self.address}"
