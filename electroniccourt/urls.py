from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^main/$', views.main_page, name='main_page'),
    url(r'^users_list/$', views.users_list_page, name='users_list_page'),
    url(r'^mail/(?P<id_mail>[0-9]+)/$', views.mail_detail, name='mail_detail'),
    url(r'^admin_page/$', views.admin_page, name='admin_page'),
    url(r'^new_user/$', views.new_user, name='new_user'),
    url(r'^creating_document/$', views.creating_document, name='creating_document'),
]
