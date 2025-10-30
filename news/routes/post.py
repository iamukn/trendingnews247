from django.views import View
from django.shortcuts import render,  redirect
from django.http import HttpResponse
from django.contrib import messages
from news.models import Posts
from django.utils.text import slugify
from django.db import transaction
from news.utils.upload_to_r2 import resize_and_upload


class Post(View):
    template_name = 'news/dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to publish a story.")
            return redirect('login')
        
        header = request.POST.get('subject').title()
        content = request.POST.get('message_area')
        category = request.POST.get('category').capitalize()
        avatar = request.FILES.get('image')
        author = request.POST.get('reporter')
        image_url = ''
        slug = slugify(header)
        date_published = request.POST.get('date')

        # upload avatar and get content type if avatar is available
        if avatar:
            content_type = avatar.content_type.split('/')[-1]
            image_key = slug + f'.{content_type}'
            image_url = f'https://pub-02de1e7975ba4bd08a7156501af173bd.r2.dev/news_photos/{image_key}'
        
        else:
            image_url = f'https://pub-02de1e7975ba4bd08a7156501af173bd.r2.dev/news_photos/default.jpg'

        if not header or not content or not category:
            messages.error(request, "All fields are required.")
            return render(request, self.template_name)
        

        try:
            # upload image to R2 instance

            

            with transaction.atomic():
                new_post = Posts(
                    header=header,
                    content=content,
                    author=author,
                    category=category,
                    image_url=image_url,
                    slug=slug,
                    date_published=date_published
                )
                new_post.save()

                if avatar:
                    image_url = resize_and_upload(avatar.read(),image_key)
        except Exception as e:
            raise e
            messages.error(request, f"An error occurred while publishing: {e}")
            return render(request, self.template_name)
        

        messages.success(request, "Story Published Successfully ✅!")
        return render(request, self.template_name)
