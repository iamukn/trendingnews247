from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
from news.models import Posts, Viewers
from django.shortcuts import get_object_or_404



class DetailsPage(TemplateView):
    
    template_name = "news/details.html"
    def get_context_data(self,slug, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Posts.objects.all()
        # data = post.get(slug=slug)
        data = get_object_or_404(Posts, slug=slug)
        context["news"] = data
        content = data.content.split('\n')
        context['paragraphs']  = content
        
        views = Viewers.objects.get(id=1)
        views.count += 1
        views.save()

        related = post.filter(category=data.category)

        context['related'] = related.order_by('-date_published')[0:3]

        return context
