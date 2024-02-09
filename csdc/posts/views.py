from django.shortcuts import render , get_object_or_404 , redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Post
from .forms import PostForm
# Create your views here.
@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html' , {'posts':posts})

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})

@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.userprofile 
            post.created_date = timezone.now()  #
            post.save()
            return redirect("posts:post_list") 
    else:
        form = PostForm()
    return render(request, 'posts/post_create.html', {'form': form})

@login_required
def post_update(request , post_id):
    post = get_object_or_404(Post, pk=post_id)  
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)  
        if form.is_valid():
            form.save()  
            return redirect('posts:post_list')  
    else:
        form = PostForm(instance=post)  
    
    return render(request, 'posts/post_update.html', {'form': form})

@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.author.user != request.user:
        return HttpResponseForbidden()
    post.delete()
    # 게시글 목록 페이지로 리다이렉트
    return redirect('posts:post_list')