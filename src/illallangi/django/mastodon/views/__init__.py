from illallangi.django.mastodon.views.home import home_html
from illallangi.django.mastodon.views.status import status_html, statuses_html

from .favicon import favicon

__all__ = [
    "favicon",
    "home_html",
    "status_html",
    "statuses_html",
]
