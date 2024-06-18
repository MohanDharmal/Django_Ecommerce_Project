import datetime

from django.db import models
from .Product import Product
from .customer import Customer


class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=400,default='',blank=True)
    phone = models.CharField(max_length=14,default='',blank=True)
    price = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_id(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

