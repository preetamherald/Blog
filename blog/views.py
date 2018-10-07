from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

# Create your views here.
def index(request):
    posts = Posts.objects.all()[:10]

    context = {
        'title':'Recent Posts',
        'posts':posts
    }

    return render(request,'blog/index.html', context)

def details(request, id):
    post = Posts.objects.get(id=id)

    context = {
    'post' : post

    }

    return render(request,'blog/details.html', context)

def main(request):
    return render(request,'blog/main.html')
