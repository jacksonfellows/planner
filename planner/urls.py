from django.conf.urls import patterns, include, url
from django.contrib import admin
from schedule import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'planner.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^([0-9][0-9][0-9][0-9])/([0-9][0-9]|[0-9])/([0-9][0-9]|[0-9])/', views.planner),

    url(r'^/', views.planner_recent),
    url(r'^', views.planner_recent),
)