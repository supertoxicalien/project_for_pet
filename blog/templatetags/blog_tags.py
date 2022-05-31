from django import template
from django.db.models import Q
from blog.models import *

register = template.Library()


@register.inclusion_tag('include/tags/search.html')
def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))
    return {'posts': posts, 'query': query}