from django.urls import include, re_path

from illallangi.django.mastodon import views

app_name = "mastodon"

urlpatterns = [
    re_path(
        "^$",
        views.home_html,
        name="home_html",
    ),
    re_path(
        "^favicon.svg$",
        views.favicon,
        name="favicon",
    ),
    re_path(
        "^favicon.ico$",
        views.favicon,
    ),
    re_path(
        "^statuses/",
        include("illallangi.django.mastodon.urls.status"),
    ),
]
