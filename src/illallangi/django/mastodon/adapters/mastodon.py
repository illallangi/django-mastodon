from typing import ClassVar

import diffsync

from illallangi.django.mastodon.diffsyncmodels import Status
from illallangi.django.mastodon.models import Status as DjangoStatus


class MastodonAdapter(diffsync.Adapter):
    Status = Status

    top_level: ClassVar = [
        "Status",
    ]

    type = "django_mastodon"

    def load(
        self,
    ) -> None:
        for obj in DjangoStatus.objects.all():
            self.add(
                Status(
                    pk=obj.pk,
                    url=obj.url,
                    content=obj.content,
                    datetime=obj.datetime,
                ),
            )
