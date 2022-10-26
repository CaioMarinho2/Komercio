from rest_framework import permissions
from rest_framework.views import Request, View

class ProductsRotesPermition(permissions.BasePermission):
    def has_permission(self, request:Request, view:View):
        return (request.method=="GET" or request.user.is_authenticated and request.user.is_seller )
    
class ProductsRotesPermitionDetail(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.method=="GET" or request.user.is_authenticated and request.user.id ==obj.seller.id )    