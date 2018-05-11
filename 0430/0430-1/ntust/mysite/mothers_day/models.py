from django.db import models

# Create your models here.
class Message(models.Model):
	author=models.CharField(max_length=20)
	title=models.CharField(max_length=100)
	content=models.TextField(max_length=300)
	publish=models.DateTimeField(auto_now=True)
	

	def __str__(self):
		return self.title+self.author
	
	
		

	