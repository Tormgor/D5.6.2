from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView  # импортируем уже знакомый generic
from django.core.paginator import Paginator
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Article, Author
from .filters import ArticleFilter
from .forms import ArticleForm

class ArticleList(ListView):
    model = Article
    template_name = 'articles.html'
    context_object_name = 'news'
    ordering = ['-datetime']
    paginate_by = 10

class SearchArticleList(ListView):
        model = Article
        template_name = 'search.html'
        context_object_name = 'news'
        ordering = ['-datetime']
        paginate_by = 10

        def get_filter(self):
            return ArticleFilter(self.request.GET, queryset=super().get_queryset())

        def get_queryset(self):
            return self.get_filter().qs

        def get_context_data(self, *args, **kwargs):
            return {
                **super().get_context_data(*args, **kwargs),
                "filter": self.get_filter(),
            }

class ArticleDetail(DetailView):
    template_name = 'article.html'
    queryset = Article.objects.all()

class ArticlePost(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_Article')
    template_name = 'add.html'
    form_class = ArticleForm

class ArticleUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.add_Article')
    template_name = 'add.html'
    form_class = ArticleForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Article.objects.get(pk=id)

class ArticleDeleteView(DeleteView):
    template_name = 'delete.html'
    queryset = Article.objects.all()
    success_url = '/news/'

