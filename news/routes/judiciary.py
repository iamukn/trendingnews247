from django.views.generic.base import TemplateView
from news.models import Posts



class JudiciaryPage(TemplateView):
    
    template_name = "news/judiciary.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        judiciary = Posts.objects.filter(category='Judiciary').order_by('-date_published')
        context["judiciary"] = judiciary
        return context
