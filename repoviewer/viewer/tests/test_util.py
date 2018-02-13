from django.test import TestCase
from ..util import GithubManager


class TestGitHubManager(TestCase):

    def test_manager(self):
        manager = GithubManager()
        token = '31a1e6f89675f93e3fba0535c4f117feca6d4af7'
        self.assertIsInstance(manager, GithubManager)
        self.assertEqual(manager.TOKEN, token)
