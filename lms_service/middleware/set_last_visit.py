from django.contrib.auth.models import User
from django.utils.timezone import now


class SetLastVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated():
            # Update last visit time after request finished processing
            User.objects.filter(pk=request.user.pk).update(last_visit=now())
        else:
            pass