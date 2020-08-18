from django import template
from blog.models import *


register = template.Library()

@register.simple_tag
def get_last_photos():
    posts = Post.objects.all().order_by('-created')[:5]
    return posts