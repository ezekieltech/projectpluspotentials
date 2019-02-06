from django.conf.urls import url


from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^projects/$', views.ProjectListView.as_view(), name='projects'),
    url(r'^projects/(?P<pk>\d+)$', views.ProjectDetailView.as_view(), name='project-detail'),
    url(r'^services/$', views.ServiceListView.as_view(), name='services'),
    url(r'^services/(?P<pk>\d+)$', views.ServiceDetailView.as_view(), name='service-detail'),
    url(r'^about-us/$', views.StaffListView.as_view(), name='about-us'),
    url(r'^about-us/(?P<pk>\d+)$', views.StaffDetailView.as_view(), name='staff-detail'),
    #url(r'^contact/$', views.contact, name='contact'),
    url('email/', views.emailView, name='email'),
    url('success/', views.successView, name='success'),

]

# used like this: <a href="{% url 'index' %}">Home</a> on the template
