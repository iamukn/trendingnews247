from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from news.models import Posts
from django.db.models import Count


class CategoriesPage(TemplateView):
    template_name = "news/categories.html"

    def get(self, request, *args, **kwargs):
        selected_category = request.GET.get('category')

        if selected_category:
            return redirect('category', category=selected_category)

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = (
            Posts.objects
            .values('category')
            .annotate(count=Count('id'))
            .order_by('-count')
        )
        return context
