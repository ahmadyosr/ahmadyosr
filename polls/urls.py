from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns=[
	
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$',views.user_login,name='login'),
	url(r'^restricted/$', views.restricted,name='restricted'),
	url(r'^logout/$', views.user_logout, name='logout'),
	
	
]
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
