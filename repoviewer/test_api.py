from github import Github


class GithubManager(Github):

    def __init__(self):
        self.TOKEN = '31a1e6f89675f93e3fba0535c4f117feca6d4af7'
        super(GithubManager, self).__init__(self.TOKEN)


if __name__ == '__main__':
    g = GithubManager()
    org = g.get_organization('githubtrainingasdfasdf')
    print(org.name)

    print(org.get_repos()[0].name)
