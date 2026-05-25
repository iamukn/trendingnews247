from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
from news.models import Posts, Viewers
from django.shortcuts import get_object_or_404
from django.core.cache import cache



class DetailsPage(TemplateView):
    
    template_name = "news/details.html"
    def get_context_data(self,slug, **kwargs):
        context = super().get_context_data(**kwargs)
        
       
        # data = post.get(slug=slug)
        article = cache.get(f'article_{slug}')
        if not article:
            article = get_object_or_404(Posts, slug=slug)
            cache.set(f'article_{slug}', article, timeout=60*60)  # Cache for 1 hour
        context["news"] = article
        content = article.content.split('\n')
        context['paragraphs']  = content
        
        views = Viewers.objects.get(id=1)
        views.count += 1
        views.save()

        # Get related
        all_articles = cache.get('all_articles')
        if not all_articles:
            all_articles = Posts.objects.all()
            cache.set('all_articles', all_articles.order_by('-date_published'), timeout=60*60)  # Cache for 1 hour
        related = all_articles.filter(category=article.category)

        context['related'] = related.order_by('-date_published')[0:3]

        return context
