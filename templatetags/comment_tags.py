from django import template

from app.modules.comments.forms import CommentForm

register = template.Library()

@register.inclusion_tag('comments/form.html', takes_context=False)
def render_comment_form(subject):
    """
    Usage: {% render_comment_form subject %}
    Renders comments/form.html with variables: form and subject
    """
    return {
        'form': CommentForm(),
        'subject': subject,
    }
