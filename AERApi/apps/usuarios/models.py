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
    institution = models.CharField(max_length=100)
    logo_src = models.CharField(max_length=255, blank=True, null=True)
    shipments = models.IntegerField()
    total_accepteds = models.IntegerField()
    intents = models.IntegerField()
    accepteds = models.IntegerField()
    problems_attempted = models.ManyToManyField(Problems, through='UsersProblemsAttempted')

    class Meta:
        db_table = 'users'


class UsersProblemsAttempted(models.Model):
    users_id = models.ForeignKey(Users, models.DO_NOTHING, db_column='id_user')
    problems_id = models.ForeignKey(Problems, models.DO_NOTHING, db_column='id_problem')
    resolved = models.BooleanField(null=False, blank=False)

    class Meta:
        db_table = 'users_problems_attempted'
        unique_together = (('users_id', 'problems_id'),)
