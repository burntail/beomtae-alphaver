from django.shortcuts import render, get_object_or_404,redirect
from .models import Blog
from django.utils import timezone

def home(request):
    blogs=Blog.objects
    return render(request, 'home.html',{'blogs':blogs})


def about(request):
    return render(request, 'about.html')

def list(request):
    blogs=Blog.objects
    return render(request, 'list.html',{'blogs':blogs})

def detail(request, blog_id):
    blog_detail=get_object_or_404(Blog, pk=blog_id )
    return render(request, 'detail.html',{'blog':blog_detail})

def create(request):
    return render(request, 'create.html')

def create_completed(request):
    blog = Blog()
    blog.title = request.GET['title']   
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/detail/'+str(blog.id))

def update(request, blog_id):
    return render(request, 'update.html',{'blog_id':blog_id})

def update_final(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    blog.title = request.GET['title']   
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()    
    return redirect('/detail/'+str(blog.id))

def delete_check(request, blog_id):
    return render(request,'delete_check.html',{'blog_id':blog_id})

def delete(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    blog.delete()
    return redirect('/list')
