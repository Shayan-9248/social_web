from rest_framework import permissions


class AuthorAccessPermission(permissions.BasePermission):
    message = 'You must be Superuser or Owner of this post'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(
            request.user.is_authenticated and
            request.user.is_superuser or 
            obj.user == request.user
        )


class IsSuperUserOrStaffOrPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_superuser or request.user.is_staff
        )