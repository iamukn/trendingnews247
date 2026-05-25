from django.views import View
from django.shortcuts import render
from news.models import Posts
from django.core.cache import cache

class SingleCategoryPage(View):
    template_name = 'news/single_category.html'

    def get(self, request, *args, **kwargs):
        category = request.GET.get('category')

        # 1️⃣ Handle missing or empty query parameter
        if not category:
            return render(request, self.template_name, {
                'category': None,
                'data': [],
                'error': "No category specified."
            })

        # 2️⃣ Normalize category name for case-insensitive matching
        category = category.strip().capitalize()

        # 3️⃣ Fetch posts safely (case-insensitive filtering)
        all_posts = cache.get('all_articles')
        if not all_posts:
            all_posts = Posts.objects.all()
            cache.set('all_articles', all_posts.order_by('-date_published'), timeout=60*60)  # Cache for 1 hour

        posts = all_posts.filter(category__iexact=category)

        # 4️⃣ Handle case where no posts exist
        if not posts.exists():
            message = f"No posts found in '{category}' category."
        else:
            message = None

        data = {
            'category': category,
            'data': posts,
            'message': message,
        }

        return render(request, self.template_name, data)