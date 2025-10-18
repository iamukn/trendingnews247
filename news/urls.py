from django.urls import path
from .routes.landing_page import LandingPage

urlpatterns = [
    path('', LandingPage.as_view(), name='landing' ),
        ]
