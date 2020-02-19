from django.db import models



class Job(models.Model):
	image    = models.ImageField(upload_to="images/")
	Brief    = models.CharField(max_length =300)
