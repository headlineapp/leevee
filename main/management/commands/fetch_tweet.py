from django.core.management.base import BaseCommand
from main.tweet_api import Tweet


class Command(BaseCommand):
    def handle(self, *args, **options):
        tweet = Tweet()
        tweet.fetch_mentions()