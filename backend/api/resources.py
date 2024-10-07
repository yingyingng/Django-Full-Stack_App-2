from import_export import resources
from api.models import GuestList
import os

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

class GuestListResource(resources.ModelResource):

    class Meta:
        model = GuestList 