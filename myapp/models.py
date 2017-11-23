from django.db import models

class Region(models.Model):
	code = models.IntegerField()
	r_name = models.CharField(max_length = 200)
	def __str__ (self):
		return self.r_name

class Tag(models.Model):
	t_name = models.CharField(max_length = 200)
	def __str__(self):
		return self.t_name

class Ad(models.Model):
	a_desc = models.TextField(max_length = 1000)
	a_region = models.ForeignKey(Region)
	a_tag = models.ForeignKey(Tag)
	def __str__(self):
		return self.a_desc

		