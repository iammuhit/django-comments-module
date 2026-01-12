from django import template
from django.contrib.contenttypes.models import ContentType

from mayacms.contrib.comments.forms import CommentForm
from mayacms.contrib.comments.models import Comment

register = template.Library()

@register.inclusion_tag('comments/index.html', takes_context=False)
def comment_list(subject):
    """
    Usage: {% comment_list subject %}
    """
    return { 'comments': Comment.objects.filter(object_id=subject.pk) }

@register.inclusion_tag('comments/form.html', takes_context=False)
def comment_form(subject):
    """
    Usage: {% comment_form subject %}
    Renders comments/form.html with variables: form, subject and subject_type
    """
    return {
        'form'        : CommentForm(),
        'subject_type': ContentType.objects.get_for_model(subject),
        'subject'     : subject,
    }

@register.simple_tag(takes_context=False)
def get_comments(*args, **kwargs):
    """
    Usage: {% get_comments subject=post as comments %}
    """
    return Comment.objects.filter(object_id=kwargs.get('subject').id)

@register.simple_tag(takes_context=False)
def get_comment_count(*args, **kwargs):
    """
    Usage: {% get_comments subject=post as comment_count %}
    """
    return Comment.objects.filter(object_id=kwargs.get('subject').id).count()
