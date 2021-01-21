from django.shortcuts import render

from rest_framework.renderers import JSONRenderer
from rest_framework import generics
from rest_framework import mixins

from .models import Product
from .serializers import ProductSerializer

#create view for list of model instances
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


#create view for list of model instances
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'name'


#create view for creating a product
class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer


#create view for updating and deleting the product instance
class ProductRetriveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'name'


class ProductRetriveDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all
    lookup_field = 'name'
        
