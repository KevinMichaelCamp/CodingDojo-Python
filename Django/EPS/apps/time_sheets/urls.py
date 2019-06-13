from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin_home$', views.admin_home, name='admin_home'),
    url(r'^clock_in$', views.clock_in, name='clock_in'),
    url(r'^clocked_in$', views.clocked_in, name='clocked_in'),
    url(r'^clock_out$', views.clock_out, name='clock_out'),
    url(r'^edit_quote$', views.edit_quote, name='edit_quote'),
    url(r'^forgot$', views.forgot, name='forgot'),
    url(r'^home$', views.home, name='home'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^points$', views.points, name='points'),
    url(r'^register$', views.register, name='register'),
    url(r'^report$', views.report, name='report'),
    url(r'^settings$', views.settings, name='settings'),
    url(r'^updates$', views.updates, name='updates'),
]
