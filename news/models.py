from django.db import models
from django.utils.text import slugify

# Create your models here.

class Posts(models.Model):
    header = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    views = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(max_length=700, unique=True, blank=False, null=False)
    image_url = models.CharField(max_length=3000, null=True, blank=True)
    category = models.CharField(max_length=50, null=False, blank=False)
    author =  models.CharField(max_length=100, null=True, blank=True)
    date_published = models.DateField()


    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.header)
            slug = base_slug
            num = 1
            while Posts.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)

class Subscribers(models.Model):
    email = models.EmailField(null=True, blank=True, unique=True)
    is_subscribed = models.BooleanField(default=False)

class Viewers(models.Model):
    count = models.IntegerField(default=0)
