from django.shortcuts import render
from rest_framework import status, mixins,viewsets
from rest_framework.response import Response
from rest_framework import generics
from .serializers import orderListSerializer
from .models import Order_List

class orderlistView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin,mixins.CreateModelMixin):
    serializer_class = orderListSerializer
    queryset = Order_List.objects.all()


class genericOrderView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = orderListSerializer
    queryset = Order_List.objects.all()

    def get(self,request):
        return self.list(request)

    def  post(self,request):
        return self.create(request)
# Create your views here.
