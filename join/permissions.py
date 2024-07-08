from rest_framework import permissions

class IsBoardUser(permissions.BasePermission):
 
    def has_object_permission(self, request,obj):
        return request.user in obj.users.all