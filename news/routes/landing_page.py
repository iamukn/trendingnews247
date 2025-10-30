from django.views.generic.base import TemplateView
from news.models import Posts



class LandingPage(TemplateView):
    
    template_name = "news/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Posts.objects.all().order_by('-date_published')
        context["latest_news"] = post[0:3]
        context['more_news'] = post[3: 20]
        return context
