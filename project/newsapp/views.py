from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Post
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

import logging

logger = logging.getLogger(__name__)

class NewsList(ListView):
    model = Post
    ordering = '-date_create'
    template_name = 'list.html'
    context_object_name = 'posts'
    paginate_by = 10


class PostDetail(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'


class PostSearch(ListView):
    model = Post
    ordering = '-date_create'
    template_name = 'search.html'
    context_object_name = 'search'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_create.html'


class NewsUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'


class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')


# class ArticleCreate(CreateView):
#     form_class = PostForm
#     model = Post
#     template_name = 'article_create.html'
#
#     def form_valid(self, form):
#         post = form.save(commit=False)
#         post.category_types = 'AR'
#         return super().form_valid(form)


# class ArticleCreate(UpdateView):
#     form_class = PostForm
#     model = Post
#     template_name = 'article_edit.html'
#
#     def form_valid(self, form):
#         post = form.save(commit=False)
#         post.category_types = 'AR'
#         return super().form_valid(form)


# class ArticleDelete(DeleteView):
#     form_class = PostForm
#     model = Post
#     template_name = 'article_delete.html'
#
#     def form_valid(self, form):
#         post = form.save(commit=False)
#         post.category_types = 'AR'
#         return super().form_valid(form)
