from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from article.models import Article,News
# Create your views here.

class ArticleListView(ListView):
    template_name = 'article/article_list.html'
    model = Article

class ArticleDetailView(DetailView):
    template_name = 'article/article_detail.html'
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['content_begin'] = Article.objects.get(pk=self.kwargs['pk']).content[:1210]
        context['content_end'] = Article.objects.get(pk=self.kwargs['pk']).content[1210:]
        return context

class NewsList(ListView):
    template_name = 'News/news_list.html'
    model = News

class NewsDetail(DetailView):
    model = News
    template_name = 'News/news_detail.html'


