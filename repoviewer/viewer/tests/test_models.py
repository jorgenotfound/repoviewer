from django.test import TestCase
from ..models import Organization, QueryStatistic
from datetime import datetime

# Create your tests here.
class TestModels(TestCase):

    def test_organization(self):
        organization_str = 'The GitHub Training Team'
        org = Organization(name='The GitHub Training Team',
                           url='https://github.com/githubtraining')
        self.assertIsInstance(org, Organization)
        self.assertEqual(organization_str, str(org))

    def test_query_statistic(self):
        now = datetime.now()
        query_txt = 'githubtraining'
        query_str = 'Fecha: {} - Busqueda: {}'.format(str(now), query_txt)
        query_statistic = QueryStatistic(query_date=now, query_text=query_txt,
                                         is_valid=True)

        self.assertIsInstance(query_statistic, QueryStatistic)
        self.assertEqual(query_str, str(query_statistic))
