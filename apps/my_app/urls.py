from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index),   
	url(r'^submit_course$', views.submit_course),
    url(r'^delete_course/(?P<id>\d+)$', views.delete_course),
    url(r'^delete_confirmation/(?P<id>\d+)$', views.delete_confirmation)
    

]