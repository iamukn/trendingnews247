from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView



class AboutUs(View):
    def get(self, request, *args, **kwargs):
        return render(template_name="news/about.html", request=request)
