from django.db import models

class Blog(models.Model):
	title      = models.CharField(max_length = 120)
	pub_date   = models.DateTimeField(auto_now_add= True)
	body       = models.TextField()
	image      = models.ImageField('images/')


	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:100]

	def pub_date_blog(self):
		return self.pub_date.strftime('%b %e %Y')