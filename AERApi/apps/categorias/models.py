from django.db import models


# Create your models here.

class Categories(models.Model):
    id_category = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    related_category = models.ForeignKey('self', models.DO_NOTHING, db_column='related_category', blank=True, null=True)

    class Meta:
        db_table = 'categories'
