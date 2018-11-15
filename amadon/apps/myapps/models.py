from __future__ import unicode_literals
from django.db import models

class Item(models.Model):
	item = models.CharField(max_length=255)
	price = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)