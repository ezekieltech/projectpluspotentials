from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

# used like this: <a href="{% url 'index' %}">Home</a> on the template
