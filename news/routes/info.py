from django.views import View
from django.shortcuts import render
from news.models import Posts

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
        posts = Posts.objects.filter(category__iexact=category)

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