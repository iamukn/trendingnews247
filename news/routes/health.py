from django.views.generic.base import TemplateView
from news.models import Posts
from django.core.cache import cache



class HealthPage(TemplateView):
    
    template_name = "news/health.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_health_articles = cache.get('all_health_articles')
        if not all_health_articles:
            all_health_articles = Posts.objects.filter(category='Health').order_by('-date_published')
            cache.set('all_health_articles', all_health_articles, timeout=60*60)  # Cache for 1 hour
        context["health"] = all_health_articles
        return context
