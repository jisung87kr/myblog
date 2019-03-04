from django.shortcuts import render
from django.http import HttpResponse

from django.utils import timezone
from .models import Post

# Create your views here.
def index(requests):
    posts = Post.objects.filter(published_date__lte = timezone.now())
    return render(requests, 'myblog/list.html', {'posts' : posts})
