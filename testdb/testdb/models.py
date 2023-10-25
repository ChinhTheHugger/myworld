from django.db import connections
from django.db import models

class People(models.Model):
    pid = models.IntegerField()
    pname = models.CharField(max_length=50)
    page = models.IntegerField()
    class Meta:
        db_table = "people"