from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from app.modules.comments.forms import CommentForm
from app.modules.comments.models import Comment
from app.modules.posts.models import Post


@login_required
def create(request):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=request.POST.get('post_pk'))
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            
            return redirect('app.modules.posts:posts.view', pk=post.pk)
    else:
        return redirect('app.modules.posts:posts.index')


@login_required
def delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('app.modules.posts:posts.view', pk=post_pk)


@login_required
def approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('app.modules.posts:posts.view', pk=comment.post.pk)
