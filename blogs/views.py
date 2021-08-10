from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import PostForm


def check_post_owner(owner, user):
    if owner != user:
        raise Http404


@login_required
def posts(request):
    posts = BlogPost.objects.filter(owner=request.user).order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)


@login_required
def new_post(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:posts')

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(id=post_id)
    check_post_owner(post.owner, request.user)

    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:posts')

    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)
