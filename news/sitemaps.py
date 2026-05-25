from django.contrib.sitemaps import Sitemap
from .models import Posts

class PostSitemap(Sitemap):
    changefreq = "hourly"
    priority = 0.8

    def items(self):
        return Posts.objects.all()

    def lastmod(self, obj):
        return obj.date_published

