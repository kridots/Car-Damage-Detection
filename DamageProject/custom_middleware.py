import re
from django.http import HttpResponseForbidden

class SuperuserRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.excluded_urls = [
            r'^/login/$',
            r'^/register/$',
            r'^/logout/$',
            r'^/password-reset/$',
            r'^/password-reset-done/',
            r'^/password-reset-confirm/',
            r'^/password-reset-complete/',
            r'^/upload/',
            r'^/api/pred_img_api',
            r'^/api/content_data_update',
            
        ]

    def __call__(self, request):
        # Check if the current URL is in the excluded URLs list
        for pattern in self.excluded_urls:
            if re.match(pattern, request.path):
                break
        else:
            if request.user.is_authenticated and not request.user.is_superuser:
                # If the user is authenticated but not a superuser,
                # return a forbidden response.
                return HttpResponseForbidden("You don't have permission to access this page.")

        # Call the next middleware in the chain or the view
        response = self.get_response(request)

        return response
