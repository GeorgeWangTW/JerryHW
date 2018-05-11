from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^add/$', views.add, name='add'),
    url(r'^save/$', views.save, name='save'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^update/$', views.update, name='update'),
    
]