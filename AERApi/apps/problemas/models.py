from django.db import models
from apps.categorias.models import Categories


# Create your models here.


class Problems(models.Model):
    id_problem = models.AutoField(primary_key=True)
    title = models.CharField(unique=True, max_length=255)
    no_repeated_accepteds = models.IntegerField()
    wrong_answer = models.IntegerField()
    accepteds = models.IntegerField()
    shipments = models.IntegerField()
    time_limit = models.IntegerField()
    memory_limit = models.IntegerField()
    presentation_error = models.IntegerField()
    attempts = models.IntegerField()
    other = models.IntegerField()
    restricted_function = models.IntegerField()
    compilation_error = models.IntegerField()
    c_shipments = models.IntegerField()
    cpp_shipments = models.IntegerField()
    java_shipments = models.IntegerField()

    class Meta:
        db_table = 'problems'


class ProblemsCategories(models.Model):
    id_problem = models.ForeignKey(Problems, models.DO_NOTHING, db_column='id_problem')
    id_category = models.ForeignKey(Categories, models.DO_NOTHING, db_column='id_category')

    class Meta:
        db_table = 'problems_categories'
        unique_together = (('id_problem', 'id_category'),)
