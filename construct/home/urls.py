from django.conf.urls import url

from .views import (ReportFormView, ProjectDetailView, ProjectListView, home, inner)


urlpatterns=[
url(r'^$', home, name='home'),
url(r'^inner/$',inner,name='inner'),

url(r'^report-form/$', ReportFormView.as_view(), name='report-form'),

url(r'^detail/project/(?P<pk>\d+)$', ProjectDetailView.as_view(), name='detail-project'),
url(r'^list/project/$', ProjectListView.as_view(), name='list-project'),

]
