from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views

urlpatterns = [
	url(r'^api/v1/', include(('reports.urls', 'reports'), namespace='reports')),
    #path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls)
]

urlpatterns += [
	url(r'^api/v1/auth', include('rest_framework.urls', namespace='rest_framework'))
]