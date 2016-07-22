from django_cron import CronJobBase, Schedule
from tweet_api import Tweet


class TwitterCronJob(CronJobBase):

    RUN_EVERY_MINUTES = 5

    schedule = Schedule(run_every_mins=RUN_EVERY_MINUTES)

    code = 'main.cron.twitter_cron_job'

    def do(self):
        tweet = Tweet()
        tweet.fetch_mentions()