from django.db import models
from apps.usuarios.models import Users


class Institutions(models.Model):
    name = models.CharField(unique=True, max_length=255)
    problems_solved = models.IntegerField()
    shipments = models.IntegerField()
    users = models.ManyToManyField(Users)
    logo_src = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'institutions'
