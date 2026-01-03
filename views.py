from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.contenttypes.models import ContentType

from app.modules.comments.forms import CommentForm
from app.modules.comments.models import Comment
from app.modules.posts.models import Post


@login_required
def create(request):
    if request.method == 'POST':
        object_id       = request.POST.get('subject_id')
        content_type_id = request.POST.get('subject_type_id')
        content_type    = get_object_or_404(ContentType, pk=content_type_id)

        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.content_type = content_type
            comment.object_id = object_id
            comment.save()
            
            return redirect(comment.content_object.get_absolute_url())
    else:
        return redirect('/')


@login_required
def delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect(comment.content_object.get_absolute_url())


@login_required
def approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect(comment.content_object.get_absolute_url())
