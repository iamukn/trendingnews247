from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from news.models import Posts



class CategoriesPage(TemplateView):
    
    template_name = "news/categories.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Posts.objects.all()
        context["politics"] = posts.filter(category='Politics').order_by('-date_published')
        context["general"] = posts.filter(category='General').order_by('-date_published')
        context["sport"] = posts.filter(category='Sport').order_by('-date_published')
        context["health"] = posts.filter(category='Health').order_by('-date_published')
        context["security"] = posts.filter(category='Security').order_by('-date_published')
        context["economic"] = posts.filter(category='Economic').order_by('-date_published')
        context["education"] = posts.filter(category='Education').order_by('-date_published')
        context["oil_and_gas"] = posts.filter(category='Oil And Gas').order_by('-date_published')
        context["foreign"] = posts.filter(category='Foreign').order_by('-date_published')
        context["agriculture"] = posts.filter(category='Agriculture').order_by('-date_published')
        context["judiciary"] = posts.filter(category='Judiciary').order_by('-date_published')
        context["entertainment"] = posts.filter(category='Entertainment').order_by('-date_published')
        context["banking"] = posts.filter(category='Banking').order_by('-date_published')
        context["religion"] = posts.filter(category='Religion').order_by('-date_published')
        return context
