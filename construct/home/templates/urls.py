from django.conf.urls import url
from home import views
from .views import home, inner


urlpatterns=[
url(r'^$',home,name='home'),
url(r'^inner/$',inner,name='inner'),
]


