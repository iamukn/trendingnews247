from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from news.models import Posts
from django.db.models import Count



class CategoryPage(TemplateView):
    
    template_name = "news/category.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = kwargs['category']
        posts = Posts.objects.all()
        context["category"] = 'Oil and Gas' if category.capitalize() == 'Oil_and_gas' else category.capitalize()
        context['posts'] = posts.filter(category=category.capitalize()).order_by('-date_published')
        print(len(context['posts']))
        return context
