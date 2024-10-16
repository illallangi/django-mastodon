from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_GET

from illallangi.django.mastodon.models.status import Status


@require_GET
def home_html(
    request: HttpRequest,
    **_: dict,
) -> render:
    base_template = "partial.html" if request.htmx else "base.html"

    return render(
        request,
        "mastodon/home.html",
        {
            "base_template": base_template,
            "page": Paginator(
                object_list=[
                    {
                        "name": "Statuses",
                        "description": "View all statuses.",
                        "a": {
                            "href": reverse("mastodon:statuses_html"),
                            "text": f"View { Status.objects.count() } Statuses",
                        },
                        "img": {
                            "src": "mastodon/statuses.png",
                            "alt": "Statuses",
                        },
                    },
                ],
                per_page=10,
            ).get_page(
                request.GET.get("page", 1),
            ),
            "breadcrumbs": [
                {
                    "title": "Mastodon",
                    "url": reverse(
                        "mastodon:home_html",
                    ),
                },
            ],
            "links": [
                {
                    "rel": "alternate",
                    "type": "text/html",
                    "href": request.build_absolute_uri(
                        reverse(
                            "mastodon:home_html",
                        ),
                    ),
                },
            ],
        },
    )
