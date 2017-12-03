from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^main/$', views.main_page, name='main_page'),
    url(r'^mail/(?P<id_mail>[0-9]+)/$', views.mail_detail, name='mail_detail'),
]