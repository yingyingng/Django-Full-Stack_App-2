from django.db import models
from django.contrib.auth.models import User
from import_export import resources


#class Note(models.Model):
    #title = models.CharField(max_length=100)
    #content = models.TextField()
    #created_at = models.DateTimeField(auto_now_add=True)
    #author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    #def __str__(self):
        #return self.title


class GuestList(models.Model):
    last_name = models.CharField(max_length=200)
    hp_num = models.IntegerField()
    table_num = models.IntegerField()
    order = models.CharField(max_length=200)

    def __str__(self):
        return self.last_name




        



