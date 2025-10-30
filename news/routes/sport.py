from django.views.generic.base import TemplateView
from news.models import Posts


class SportPage(TemplateView):
    
    template_name = "news/sport.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sport = Posts.objects.filter(category='Sport').order_by('-date_published')
        context["sport"] = sport
        return context
