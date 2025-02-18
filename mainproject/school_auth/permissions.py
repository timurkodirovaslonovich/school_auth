from rest_framework.permissions import BasePermission

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

from rest_framework.permissions import BasePermission

class IsTeacherOrSuperUser(BasePermission):
    def has_permission(self, request, view):
        # Ensure the user is authenticated before checking the role
        # if not request.user.is_authenticated:
        #     return False  # If the user is not authenticated, deny access
        #
        if request.user.is_authenticated or request.user.role == 'teacher':
            return True

        # # Allow access if the user is a teacher or superuser
        # return request.user.role == 'teacher' or request.user.role == 'superuser'
