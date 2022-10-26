from rest_framework import serializers

from user.serializers import SellerProductSerializer
from .models import Product



class ProductSerializer(serializers.ModelSerializer):
    
    seller= SellerProductSerializer(read_only=True)
    class Meta:
        model = Product
        fields=["id","seller","description","price","quantity","is_active"]
        
 
class ProductGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=["description","price","quantity","is_active","seller_id"] 
    
class ProductGeneralDetailSerializer(serializers.ModelSerializer):
    seller= SellerProductSerializer(read_only=True)
    class Meta:
        model = Product
        fields=["description","price","quantity","is_active","seller"]    