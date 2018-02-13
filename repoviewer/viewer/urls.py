from django.conf.urls import url
from viewer.views import HomeView, OrganizationDetailView, InvalidQueryView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home_view'),
    url(r'^invalid_query$', InvalidQueryView.as_view(), name='invalid_query'),
    url(r'^organization/(?P<pk>\w+)', OrganizationDetailView.as_view(),
        name='organization_detail'),
]