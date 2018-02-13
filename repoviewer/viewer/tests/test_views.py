from datetime import datetime
from unittest import skip
from django.urls import reverse
from django.test import TestCase
from ..forms import HomeQueryForm
from ..models import QueryStatistic


class TestHomeView(TestCase):

    def test_home_view_first_time_visit(self):
        response = self.client.get(reverse('home_view'))
        self.assertContains(response, '<title>Buscar organización</title>')
        self.assertContains(response, 'No ha hecho ninguna consulta')
        query_form = response.context_data['form']
        self.assertIsInstance(query_form, HomeQueryForm)

    def test_home_view_with_previous_queries(self):
        now = datetime.now()
        query_txt = 'githubtraining'
        query_statistic = QueryStatistic(query_date=now, query_text=query_txt,
                                         is_valid=True)
        query_statistic.save()
        response = self.client.get(reverse('home_view'))
        self.assertContains(response, '<title>Buscar organización</title>')
        self.assertContains(response, query_txt)

    def test_home_view_invalid_login(self):
        data = {'query': 'asdf'}
        response = self.client.post(
            reverse('home_view'), data=data, follow=True
        )
        self.assertContains(
            response, '<title>No se encontró un resultado</title>')
        self.assertContains(
            response, 'El criterio de busqueda no arrojó ningun resultado')

    def test_home_view_valid_login(self):
        data = {'query': 'githubtraining'}
        response = self.client.post(
            reverse('home_view'), data=data, follow=True
        )
        self.assertContains(
            response, '<title>Detalles de la organización</title>')
        self.assertContains(
            response, 'The GitHub Training Team')


class TestInvalidQueryView(TestCase):

    def test_invalid_query_view(self):
        response = self.client.get(reverse('invalid_query'))
        self.assertContains(
            response, '<title>No se encontró un resultado</title>')
        self.assertContains(
            response, 'El criterio de busqueda no arrojó ningun resultado')


@skip('sin implementar')
class TestOrganizationDetailView(TestCase):
    pass
