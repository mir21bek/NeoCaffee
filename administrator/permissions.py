from rest_framework import permissions


class IsAdminUser(permissions.BasePermission):
    """
    Разрешение на проверку, является ли пользователь администратором.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == "admin"
        )


class IsClientUser(permissions.BasePermission):
    """
    Разрешение на проверку, является ли пользователь клиентом.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == "client"
        )
