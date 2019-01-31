from rest_framework import generics
from .models import Report
from .serializers import ReportSerializer
from django.shortcuts import get_object_or_404

class ReportList(generics.ListCreateAPIView):
	queryset = Report.objects.all()
	serializer_class = ReportSerializer

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(
			queryset,
			pk=self.kwargs['pk'],
		)
		return obj