from django.conf.urls import url
from.import views

urlpatterns=[

	url(r'^$',views.writing_forms,name='writing_forms'),
	url(r'^mothers_day/writing$',views.writing,name='writing'),

]