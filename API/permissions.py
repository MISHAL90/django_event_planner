from rest_framework.permissions import BasePermission


class Event_Permissions(BasePermission):

	def has_object_permission(self, request, view, obj):
		if request.user == obj.organizer:
			print ("noooop")
			return True
		print (" okay")

		return False