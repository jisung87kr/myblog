import math
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator

from django.utils import timezone
from .models import Post
from .form import PostForm

# Create your views here.
def index(request):
    posts = Post.objects.filter(published_date__lte = timezone.now())
    if request.GET.get('page'):
        page = int(request.GET.get('page'))
    else :
        page = int(1)
    p_range = int(5)
    paginator = Paginator(posts, p_range)
    current_block = math.ceil(page/p_range)
    start_block = (current_block-1)*p_range
    end_block = start_block+p_range
    page_range = paginator.page_range[start_block:end_block]
    posts = paginator.get_page(page)
    return render(request, 'myblog/list.html', {
        'posts' : posts,
        'page_range' : page_range,
        })

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'myblog/post.html', {'post' : post})
    
def write(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('myblog:post', args=(post.pk,)))
    else :
        form = PostForm()
    return render(request, 'myblog/write.html', {'form' : form})

def modi(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('myblog:post', args=(post.pk,)))
    else :
        form = PostForm(instance=post)
    return render(request, 'myblog/write.html', {'form' : form})

    
def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return HttpResponseRedirect( reverse('myblog:index') )
