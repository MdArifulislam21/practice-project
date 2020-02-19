from django.db import models

class Blog(models.Model):
	title      = models.CharField(max_length = 120)
	pub_date   = models.DateTimeField(auto_now_add= True)
	body       = models.TextField(max_length=500)
	image      = models.ImageField()

