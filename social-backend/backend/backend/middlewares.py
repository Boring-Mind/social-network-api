from typing import Final

from django.core.cache import cache
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin


class UpdateLastActivityMiddleware(MiddlewareMixin):
    LAST_ACTIVITY_CACHE_TEMPLATE: Final[str] = "last_activity__user_{user_id}"
    # 30 days
    DEFAULT_CACHE_TIMEOUT: Final[int] = 30 * 24 * 60 * 60

    def process_response(self, request, response):
        if hasattr(request, "user"):
            if request.user.is_authenticated:
                cache.set(
                    self.LAST_ACTIVITY_CACHE_TEMPLATE.format(user_id=request.user.id),
                    timezone.now(),
                    timeout=self.DEFAULT_CACHE_TIMEOUT,
                )
        return response
