from django.views.generic.base import TemplateView
from news.models import Posts
from django.core.cache import cache



class JudiciaryPage(TemplateView):
    
    template_name = "news/judiciary.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        judiciary = cache.get('all_judiciary_articles')
        if not judiciary:
            judiciary = Posts.objects.filter(category='Judiciary').order_by('-date_published')
            cache.set('all_judiciary_articles', judiciary, timeout=60*60)  # Cache for 1 hour
        context["judiciary"] = judiciary
        return context
