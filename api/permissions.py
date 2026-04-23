from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
       """
       Разрешает чтение всем, но редактирование (POST, PATCH, DELETE) — только админам.
       """
       def has_permission(self, request, view):
              if request.method in permissions.SAFE_METHODS:
                     return True
              return bool(request.user and request.user.is_staff)
       
       
class IsOwnerOrAdmin(permissions.BasePermission):
       """
       Разрешает доступ только владельцу объекта или администратору.
       """
       def has_object_permission(self, request, user_obj, obj):
              if request.user.is_staff:
                     return True
              return obj.client == request.user
       
       

