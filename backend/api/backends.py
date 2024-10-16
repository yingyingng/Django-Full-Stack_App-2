
from django.contrib.auth.backends import BaseBackend
from django.core.exceptions import ObjectDoesNotExist
from .models import GuestList

class GuestListBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            # Attempt to find a matching record in the GuestList table
            guest = GuestList.objects.get(username=username, password=password)
        
            return guest  # Return the guest object if authenticated
        except GuestList.DoesNotExist:
            return None  # Return None if authentication fails

    def get_user(self, user_id):
        # This method is required to retrieve a user instance using their ID
        try:
            return GuestList.objects.get(pk=user_id)
        except GuestList.DoesNotExist:
            return None
