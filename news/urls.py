from django.urls import path
from .routes.landing_page import LandingPage
from .routes.politics import PoliticsPage
from .routes.judiciary import JudiciaryPage
from .routes.health import HealthPage
from .routes.categories import CategoriesPage
from .routes.details import DetailsPage
from .routes.sport import SportPage
from .routes.about import AboutUs
from .routes.auth import Login, Subscribe
from .routes.dashboard import Dashboard
from .routes.post import Post
from .routes.info import SingleCategoryPage

urlpatterns = [
    path('', LandingPage.as_view(), name='landing' ),
    path('about-us/', AboutUs.as_view(), name='aboutus' ),
    path('categories/', CategoriesPage.as_view(), name='categories' ),
    path('category/', SingleCategoryPage.as_view(), name='category' ),
    path('subscribe/', Subscribe.as_view(), name='subscribe' ),
    path('login/', Login.as_view(), name='login' ),
    path('dashboard/', Dashboard.as_view(), name='dashboard' ),
     path('post/', Post.as_view(), name='post' ),
    path('<str:slug>/', DetailsPage.as_view(), name='details' ),
        ]
