from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from blog.models import Category, Post


class CategorySitemaps(Sitemap):
    def items(self):
        return Category.objects.all()


class PostSitemaps(Sitemap):
    def items(self):
        return Post.objects.filter(status=Post.ACTIVE)

    def lastmod(self, obj):
        return obj.create_at