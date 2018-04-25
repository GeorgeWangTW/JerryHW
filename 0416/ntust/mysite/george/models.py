from django.db import models


# Create your models here.
class Person(models.Model):
	name=models.CharField(max_length=20)
	birthday=models.DateTimeField()
	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        )
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	starsigns=models.CharField(max_length=20)
	phone_number=models.CharField(max_length=10)

	def __str__(self):
		return self.name



