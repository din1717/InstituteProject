from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if not request.user.is_superuser and view.action in ['create','update','retrieve','list']:
            return True

    def has_object_permission(self, request, view, obj):
        if not request.user.is_superuser:
            return obj.userid == request.user