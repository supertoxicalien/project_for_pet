from django.urls import path
from .views import index, detail, category, Search, AllBlogPosts


urlpatterns = [
    path('', index, name='index'),
    path('allblog', AllBlogPosts.as_view(), name='all_blog_posts'),
    path('<slug:slug>', category, name='category'),
    path('<slug:category_slug>/<slug:slug>/', detail, name='detail'),
    path('search/', Search.as_view(), name='search'),

]