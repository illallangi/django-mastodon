from django.core.management.base import BaseCommand

from illallangi.django.mastodon.adapters import MastodonAdapter as DjangoMastodonAdapter
from illallangi.mastodon.adapters import MastodonAdapter as MastodonMastodonAdapter


class Command(BaseCommand):
    help = "Sync Mastodon data from one adapter to another."
    requires_migrations_checks = True

    def handle(
        self,
        *_args: tuple,
        **_kwargs: dict,
    ) -> None:
        src = MastodonMastodonAdapter()
        dst = DjangoMastodonAdapter()

        src.load()
        dst.load()

        src.sync_to(dst)

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully synchronised.",
            ),
        )
