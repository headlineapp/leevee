from main.twitter import *
from main.models import User, Tweet
from TweetBot.settings import \
    TWITTER_ACCESS_TOKEN, \
    TWITTER_CONSUMER_SECRET, \
    TWITTER_CONSUMER_KEY, \
    TWITTER_TOKEN_SECRET


class Tweet(object):

    def __init__(self):
        self.api = Twitter(auth=OAuth(TWITTER_ACCESS_TOKEN,
                                      TWITTER_TOKEN_SECRET,
                                      TWITTER_CONSUMER_KEY,
                                      TWITTER_CONSUMER_SECRET))

    def fetch_mentions(self):
        last_tweet = Tweet.objects.all().first()
        if last_tweet:
            mentions = self.api.statuses.mentions_timeline(since_id=last_tweet.tweet_id)
        else:
            mentions = self.api.statuses.mentions_timeline()
        for mention in mentions:
            user, created = User.objects.get_or_create(user_id=mention['user']['id'])
            if created:
                user.name = mention['user']['name']
                user.screen_name = mention['user']['screen_name']
                user.location = mention['user']['location']
                user.description = mention['user']['description']
                user.profile_image_url = mention['user']['profile_image_url']
                user.save()

            tweet, created = Tweet.objects.get_or_create(tweet_id=tweet['id'])
            if created:
                tweet.created_at = tweet['created_at']
                tweet.text = tweet['text']
                tweet.source = tweet['source']
                tweet.in_reply_to_status_id = tweet['in_reply_to_status_id']
                tweet.in_reply_to_user_id = tweet['in_reply_to_user_id']
                tweet.in_reply_to_screen_name = tweet['in_reply_to_screen_name']
                tweet.save()
