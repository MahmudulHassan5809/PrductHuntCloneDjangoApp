from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField(blank=True)
	image = models.ImageField(upload_to='product/%Y/%m/%d/')
	icon = models.ImageField(upload_to='product/%Y/%m/%d/')
	url = models.TextField(blank=True)
	votes_total = models.IntegerField(default=1)
	pub_date = models.DateTimeField(default=datetime.now , blank=True)
	hunter = models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:100] + '.....'

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')
