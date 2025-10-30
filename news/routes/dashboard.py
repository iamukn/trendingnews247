from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,  redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

class Dashboard(LoginRequiredMixin, View):
    template_name = 'news/dashboard.html'
    login_url = '/login/'    

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)