from django.db import models


# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=100)
    login = models.CharField(max_length=100, unique=True, default='')
    url = models.URLField()

    class Meta:
        verbose_name = 'Organizacion'
        verbose_name_plural = 'Organizaciones'
        db_table = 'blizuu_orgs'

    def __str__(self):
        return self.name


# class Repository(models.Model):
#     pass


class QueryStatistic(models.Model):
    query_date = models.DateTimeField(auto_now_add=True)
    query_text = models.CharField(max_length=100)
    is_valid = models.BooleanField()

    class Meta:
        verbose_name = 'Consulta API'
        verbose_name_plural = 'Consultas API'
        db_table = 'blizuu_queries'

    def __str__(self):
        return 'Fecha: {} - Busqueda: {}'.format(self.query_date,
                                                 self.query_text)
