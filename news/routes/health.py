from django.views.generic.base import TemplateView
from news.models import Posts



class HealthPage(TemplateView):
    
    template_name = "news/health.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        health = Posts.objects.filter(category='Health').order_by('-date_published')
        context["health"] = health
        return context
