from django.views.generic.base import TemplateView
from news.models import Posts



class PoliticsPage(TemplateView):
    
    template_name = "news/politics.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        politics = Posts.objects.filter(category='Politics').order_by('-date_published')
        context["politics"] = politics
        return context
