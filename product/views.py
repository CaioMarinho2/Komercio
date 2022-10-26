from rest_framework import generics
from .permissions import ProductsRotesPermition,ProductsRotesPermitionDetail
from utils.mixins import SerializerByMethodMixin
from rest_framework.authentication import TokenAuthentication
from .serializers import ProductGeneralSerializer, ProductSerializer,ProductGeneralDetailSerializer
from .models import Product


class ProductView(SerializerByMethodMixin,generics.ListCreateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[ProductsRotesPermition]
    
    queryset= Product.objects.all()    
    
    serializer_map = {
        'GET': ProductGeneralSerializer,
        'POST': ProductSerializer,
    }
    
    def perform_create(self, serializer):
        return serializer.save(seller=self.request.user)
    
class ProductViewDetail(SerializerByMethodMixin,generics.RetrieveUpdateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[ProductsRotesPermitionDetail]
    
    queryset= Product.objects.all()    
    
    serializer_map = {
        'GET': ProductGeneralDetailSerializer,
        'PATCH': ProductSerializer,
    }