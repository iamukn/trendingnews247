from django.views.generic.base import TemplateView
from news.models import Posts
from django.core.cache import cache



class LandingPage(TemplateView):
    
    template_name = "news/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_articles = cache.get('all_articles')
        if not all_articles:
            all_articles = Posts.objects.all().order_by('-date_published')
            cache.set('all_articles', all_articles, timeout=60*60)  # Cache for 1 hour
        context["latest_news"] = all_articles[0:3]
        context['more_news'] = all_articles[3: 13]
        return context
