from django.test import TestCase
from ..models import Organization, QueryStatistic
from datetime import datetime

# Create your tests here.
class TestModels(TestCase):

    def setUp(self):
        self.organization_str = 'The GitHub Training Team'

    def test_organization(self):

        org = Organization(name='The GitHub Training Team',
                           url='https://github.com/githubtraining')
        self.assertIsInstance(org, Organization)
        self.assertEqual(self.organization_str, str(org))

    def test_get_organization_data(self):
        org = Organization.get_organization_data('githubtraining')
        self.assertIsInstance(org, Organization)
        self.assertEqual(self.organization_str, str(org))
        repos = org.repository_set.all()
        self.assertEqual(len(repos), 32)

    def test_query_statistic(self):
        now = datetime.now()
        query_txt = 'githubtraining'
        query_str = 'Fecha: {} - Busqueda: {}'.format(str(now), query_txt)
        query_statistic = QueryStatistic(query_date=now, query_text=query_txt,
                                         is_valid=True)

        self.assertIsInstance(query_statistic, QueryStatistic)
        self.assertEqual(query_str, str(query_statistic))
