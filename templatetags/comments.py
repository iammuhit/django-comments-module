from django import template

from app.modules.comments.forms import CommentForm

register = template.Library()

@register.inclusion_tag('comments/form.html', takes_context=False)
def comment_form(subject):
    """
    Usage: {% comment_form subject %}
    Renders comments/form.html with variables: form and subject
    """
    return {
        'form': CommentForm(),
        'subject': subject,
    }
