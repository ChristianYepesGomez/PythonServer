from django.db import models
from apps.problemas.models import Problems


class BlacklistUsers(models.Model):
    id_blacklist = models.AutoField(primary_key=True)
    number_user = models.IntegerField(unique=True)

    class Meta:
        db_table = 'blacklist_users'


class Users(models.Model):
    id_user = models.AutoField(primary_key=True)
    nick = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    institution = models.CharField("apps.institutions.model.Institutions", max_length=100)
    logo_src = models.CharField(max_length=255, blank=True, null=True)
    shipments = models.IntegerField()
    total_accepteds = models.IntegerField()
    intents = models.IntegerField()
    accepteds = models.IntegerField()
    problems_solved = models.ManyToManyField(Problems, related_name="problems_solved")
    problems_attempted = models.ManyToManyField(Problems, related_name="problems_attempted")

    class Meta:
        db_table = 'users'
