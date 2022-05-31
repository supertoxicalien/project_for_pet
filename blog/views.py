from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .forms import CommentForm
from blog.models import Post, Category


def index(request):
    post = Post.objects.filter(status=Post.ACTIVE)
    context = {
        'posts': post
    }
    return render(request, 'index.html', context=context)


def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('detail', category_slug=category_slug, slug=slug)
    else:
        form = CommentForm()

    return render(request, 'blog-single.html', {'post': post, 'form': form})


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)

    return render(request, 'category.html', {'category': category, 'posts': posts})


class AllBlogPosts(ListView):
    model = Post
    queryset = Post.objects.filter(status=Post.ACTIVE)
    template_name = 'blog-2.html'


class Search(ListView):
    paginate_by = 4
    template_name = 'blog-2.html'

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get("s"), status=Post.ACTIVE)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["s"] = self.request.GET.get("s")
        return context


def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]

    return HttpResponse("\n".join(text), content_type="text/plain")