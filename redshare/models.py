from django.db import models

# Create your models here.

class Member(models.Model):
	name = models.CharField(max_length=20)
	blood_group = models.CharField(max_length=5)
	phone_number = models.CharField(max_length=15)
	place = models.CharField(max_length=50)