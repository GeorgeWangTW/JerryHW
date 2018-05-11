from __future__ import unicode_literals
from django.shortcuts import render_to_response
from django.utils import timezone
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Post
from . import models
import datetime
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
def add(request):
	return render_to_response('blog/add_blog.html')	

def save(request):
	try:
		request.encoding='utf-8'
		author=request.GET.get('author')
		title=request.GET.get('title')
		content = request.GET.get('content')
		created = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		publish = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		message=models.Post(author=author,title=title,text=content,created_date=created,published_date=publish)	
		message.save()
		return HttpResponseRedirect('/blog/')
	except:
		print("您的操作失敗了，請重新操作")
		return HttpResponseRedirect('/blog/')
def edit(request):
	try:
		article_id=request.GET.get('id')
		posts=Post.objects.filter(id=article_id)
		return render(request, 'blog/edit_blog.html', {'posts': posts})
	except:
		print("您的操作失敗了，請重新操作")
		return HttpResponseRedirect('/blog/')
def update(request):
		update_id=request.GET['id']
		updatePost=Post.objects.get(id=update_id)
		updatePost.author=request.GET.get("author")
		updatePost.title=request.GET.get("title")
		updatePost.text=request.GET.get("content")
		updatePost.published_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		updatePost.save()
		return HttpResponseRedirect('/blog/')
def delete(request):
	try:
		deleted_id=request.GET["id"]
		post = Post.objects.get(id=deleted_id)
		post.delete()
		return HttpResponseRedirect('/blog/')
	except:
		print("您的操作失敗了，請重新操作")
		return HttpResponseRedirect('/blog/')	