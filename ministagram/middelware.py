"""MinInstagram Middleware"""

# Django
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:

    def __init__(self, get_response):
        """Middleware initialization"""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before"""
        if not request.user.is_anonymous:
            profile = request.user.profile
            if not profile.picture:
                if request.path not in [reverse('update_profile'), reverse('logout')]:
                    return redirect('update_profile')

        response = self.get_response(request)
        return response
