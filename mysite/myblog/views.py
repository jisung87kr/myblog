from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect

from django.utils import timezone
from .models import Post
from .form import PostForm

# Create your views here.
def index(request):
    posts = Post.objects.filter(published_date__lte = timezone.now())
    return render(request, 'myblog/list.html', {'posts' : posts})

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'myblog/post.html', {'post' : post})
    
def write(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
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
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('myblog:post', args=(post.pk,)))
    else :
        form = PostForm(instance=post)
    return render(request, 'myblog/write.html', {'form' : form})
