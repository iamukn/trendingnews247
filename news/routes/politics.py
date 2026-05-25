from django.views.generic.base import TemplateView
from news.models import Posts
from django.core.cache import cache



class PoliticsPage(TemplateView):
    
    template_name = "news/politics.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        politics = cache.get('all_politics_articles')
        if not politics:
             politics = Posts.objects.filter(category='Politics').order_by('-date_published')
             cache.set('all_politics_articles', politics, timeout=60*60)  # Cache for 1 hour
        context["politics"] = politics
        return context
