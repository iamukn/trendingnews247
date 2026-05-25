from django.views.generic.base import TemplateView
from news.models import Posts
from django.core.cache import cache


class SportPage(TemplateView):
    
    template_name = "news/sport.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sport = cache.get('all_sport_articles')
        if not sport:
            sport = Posts.objects.filter(category='Sport').order_by('-date_published')
            cache.set('all_sport_articles', sport, timeout=60*60)  # Cache for 1 hour
        context["sport"] = sport
        return context
