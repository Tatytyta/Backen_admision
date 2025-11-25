from rest_framework import permissions


class IsAdminUser(permissions.BasePermission):
    """
    Permiso personalizado para permitir solo a administradores.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_staff


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permiso que permite a usuarios normales solo lectura (GET, HEAD, OPTIONS)
    y a administradores acceso completo (POST, PUT, PATCH, DELETE).
    """
    def has_permission(self, request, view):
        # Los usuarios autenticados pueden leer
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        
        # Solo administradores pueden crear, editar o eliminar
        return request.user and request.user.is_authenticated and request.user.is_staff


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Permiso que permite a los usuarios editar solo sus propios objetos,
    mientras que los administradores pueden editar cualquier objeto.
    """
    def has_object_permission(self, request, view, obj):
        # Los administradores tienen acceso total
        if request.user.is_staff:
            return True
        
        # Los usuarios normales solo pueden leer
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Para escritura, verificar si el objeto pertenece al usuario
        # Esto asume que el modelo tiene un campo 'user' o similar
        return hasattr(obj, 'user') and obj.user == request.user
