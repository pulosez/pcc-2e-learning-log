from django.shortcuts import render, redirect

from .models import BlogPost
from .forms import PostForm


def posts(request):
    posts = BlogPost.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)


def new_post(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:posts')

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


def edit_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)

    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:posts')

    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)
