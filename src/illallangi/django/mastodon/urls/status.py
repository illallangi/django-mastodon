from django.urls import re_path

from illallangi.django.mastodon import views

urlpatterns = [
    re_path(
        "^$",
        views.statuses_html,
        name="statuses_html",
    ),
    re_path(
        r"^(?P<status_year>[0-9]{4})/$",
        views.statuses_html,
        name="statuses_year",
    ),
    re_path(
        r"^(?P<status_year>[0-9]{4})/(?P<status_month>[0-9]{2})/$",
        views.statuses_html,
        name="statuses_month",
    ),
    re_path(
        r"^(?P<status_year>[0-9]{4})/(?P<status_month>[0-9]{2})/(?P<status_day>[0-9]{2})/$",
        views.statuses_html,
        name="statuses_day",
    ),
    re_path(
        r"^(?P<status_year>[0-9]{4})/(?P<status_month>[0-9]{2})/(?P<status_day>[0-9]{2})/(?P<status_slug>[\w\d-]+)/$",
        views.status_html,
        name="status_html",
    ),
]
