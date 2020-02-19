from django.db import models



class Job(models.Model):
	image    = models.ImageField(upload_to="images/")
	brief    = models.CharField(max_length =300)
