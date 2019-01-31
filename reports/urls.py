from django.conf.urls import url
from reports.views import *

urlpatterns = [
	url(r'^reports/$', ReportList.as_view(), name='reports')
]