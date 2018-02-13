from django.db import models
from .util import GithubManager
from github.GithubException import UnknownObjectException


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

    @staticmethod
    def get_organization_data(login):
        g = GithubManager()
        organization_data = g.get_organization(login)

        try:
            organization_object = Organization.objects.get(login=login)
        except Organization.DoesNotExist:
            organization_object = Organization.objects.create(
                name=organization_data.name, url=organization_data.url,
                login=organization_data.login)
        finally:
            # repositories
            repos = organization_data.get_repos()
            repo_objects = []
            for repo in repos:
                repo_objects.append(Repository(
                    name=repo.full_name, created_at=repo.created_at,
                    last_updated=repo.updated_at, url=repo.url,
                    organization=organization_object)
                )
            Repository.objects.bulk_create(repo_objects)
            return organization_object


class Repository(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    last_updated = models.DateTimeField()
    url = models.URLField()
    organization = models.ForeignKey(Organization)

    class Meta:
        verbose_name = 'Repositorio'
        verbose_name_plural = 'Repositorios'
        db_table = 'blizuu_repos'


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
