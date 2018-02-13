from django.urls.base import reverse_lazy
from django.views.generic import DetailView
from django.views.generic import FormView
from django.views.generic import TemplateView
from github.GithubException import UnknownObjectException

from .forms import HomeQueryForm
from .util import GithubManager
from .models import Organization, QueryStatistic



class HomeView(FormView):
    template_name = 'viewer/index.html'
    form_class = HomeQueryForm

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        try:
            context['latest_query'] = QueryStatistic.objects.latest(
                'query_date')
        except QueryStatistic.DoesNotExist:
            pass
        return context

    def form_valid(self, form):
        login = form.cleaned_data.get('query')
        last_query = QueryStatistic(query_text=login, is_valid=True)
        last_query.save()
        g = GithubManager()
        try:
            organization_data = g.get_organization(login)

            try:
                org = Organization.objects.get(login=login)
            except Organization.DoesNotExist:
                org = Organization(name=organization_data.name,
                                   url=organization_data.url,
                                   login=organization_data.login)
                org.save()
            finally:
                # repositories
                self.success_url = reverse_lazy('organization_detail',
                                                kwargs={'pk': org.pk})
        except UnknownObjectException:
            self.success_url = reverse_lazy('invalid_query')

        return super(HomeView, self).form_valid(form)


class InvalidQueryView(TemplateView):
    template_name = 'viewer/invalid_query.html'


class OrganizationDetailView(DetailView):
    model = Organization
    template_name = 'viewer/organization.html'
    context_object_name = 'organization'

