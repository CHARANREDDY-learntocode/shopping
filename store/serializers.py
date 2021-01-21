from rest_framework import serializers
from .models import Product

#define the serializer for product model
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'