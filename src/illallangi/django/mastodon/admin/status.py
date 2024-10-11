from django.contrib.admin import ModelAdmin, register

from illallangi.django.mastodon.models import Status


@register(Status)
class StatusModelAdmin(ModelAdmin):
    pass
