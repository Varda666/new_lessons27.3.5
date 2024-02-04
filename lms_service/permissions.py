from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):

    def has_permission(self, request, view):
        if request.user.user_role == 'moderator':
            return True
        return False


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False


class IsOwnerOrNot(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        else:
            return obj.email, obj.first_name, obj.country, obj.img

