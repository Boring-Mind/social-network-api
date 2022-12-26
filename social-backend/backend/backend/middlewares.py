from typing import Final

from django.core.cache import cache
from django.utils import timezone


class UpdateLastActivityMiddleware(object):
    LAST_ACTIVITY_CACHE_TEMPLATE: Final[str] = "last_activity__user_{user_id:s}"

    def process_view(self, request, view_func, view_args, view_kwargs):
        if hasattr(request, "user"):
            if request.user.is_authenticated():
                cache.set(
                    self.LAST_ACTIVITY_CACHE_TEMPLATE.format(user_id=request.user.id),
                    timezone.now(),
                    # 30 days
                    timeout=30 * 24 * 60 * 60,
                )
