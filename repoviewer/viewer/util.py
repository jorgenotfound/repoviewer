from github import Github


class GithubManager(Github):
    """ wrapper class to PyGithub main class"""

    def __init__(self):
        self.TOKEN = '31a1e6f89675f93e3fba0535c4f117feca6d4af7'
        super(GithubManager, self).__init__(self.TOKEN)
