from rest_framework import permissions
from rest_framework.views import Request, View

class UsePatchRotePermition(permissions.BasePermission):
    def has_object_permission(self, request:Request, view:View, obj):
        return request.user.is_authenticated and obj.id==  request.user.id

class UsePatchRotePermitionDetail(permissions.BasePermission):
    def has_object_permission(self, request:Request, view:View, obj):
        return request.user.is_authenticated and request.user.is_superuser    
