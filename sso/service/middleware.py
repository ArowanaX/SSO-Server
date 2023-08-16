from django.utils import timezone
from django.core.cache import cache
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin


class RateLimiterMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        user_ip = request.META['REMOTE_ADDR']
        key = f"rate_limit:{user_ip}"
        now = timezone.now()
        last_request_time = cache.get(key)

        if last_request_time is not None:
            if (now - last_request_time).seconds < 60:
                return JsonResponse({"error": "Too many requests, please try again later."}, status=429)

        cache.set(key, now, 60)  # expire the cache key after 60 seconds