from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from . import models
from .models import Message
import datetime
# Create your views here.


def writing_forms(request):
	mg=Message.objects.all()
	return render_to_response('mothers_day/blogs_form.html',locals())
def writing(request):
	request.encoding='utf-8'
	author=request.GET['author']
	content=request.GET['content']
	title=request.GET['title']
	publish=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	message=models.Message(title=title,author=author,content=content,publish=publish)
	message.save()
	return HttpResponseRedirect('/mothers_day/')