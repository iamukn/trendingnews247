from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,  redirect
from django.contrib import messages
from django.db import transaction, IntegrityError
from news.models import Subscribers

class Login(View):
    template_name = 'news/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # authenticate by username or email
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # ✅ this creates the session
            print('Login successful')
            messages.success(request, "Login successful!")
            return redirect('dashboard')  # or wherever you want
        else:
            messages.error(request, "Invalid credentials")
            return render(request, self.template_name)

class Subscribe(View):
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')


        try:

            with transaction.atomic():
                subscriber = Subscribers(
                    email=email.lower(),
                    is_subscribed=True
                )

                subscriber.save()
                print(email)
                return JsonResponse({'success': f'{email} subscribed'}, status=200)
        
        except IntegrityError:
            # Duplicate email or unique constraint error
            return JsonResponse({'error': f'{email} is already subscribed.'}, status=400)
        
        except Exception as e:
            return JsonResponse({'error': f'{str(e)}'}, status=400)