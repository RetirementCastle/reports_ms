from django.db import models

class Report(models.Model):
	name=models.CharField(max_length=50)
	r_type=models.CharField(max_length=50)
	ip=models.CharField(max_length=15)