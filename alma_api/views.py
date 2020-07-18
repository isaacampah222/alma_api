from django.shortcuts import render
from rest_framework import status, mixins,viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import orderListSerializer
from .models import Order_List

class orderlistView(viewsets.ModelViewSet):
    serializer_class = orderListSerializer
    queryset = Order_List.objects.all()



# Create your views here.
