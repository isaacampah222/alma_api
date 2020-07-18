from rest_framework import serializers
from .models import Order_List

class orderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_List
        fields  = ['customer_id','customer_name','single_order_value']
