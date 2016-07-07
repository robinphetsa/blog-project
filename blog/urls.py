from django.conf.urls import url

from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^category/(?P<pk>\d+)/$', views.post_category, name='post_category'),
    url(r'^about', TemplateView.as_view(template_name='blog/about_me.html'),name='about'),
    ]