from django.db import models

class Order_List(models.Model):
    customer_id=models.CharField(max_length=10)
    customer_name= models.CharField(max_length=100)
    single_order_value = models.CharField(max_length=250)

    def __str__(self):
        return self.customer_id