from __future__ import unicode_literals

from django.db import models


CATEGORY_CHOICES = (
    (0, 'Confirmation / Verification'),
    (1, 'Tracking'),
    (2, 'Refund'),
    (3, 'Status Order'),
    (4, 'OTP'),
)


class UserMention(models.Model):
    screen_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    mention_id = models.IntegerField()


class Entity(models.Model):
    user_mentions = models.ManyToManyField(UserMention)

    class Meta:
        verbose_name_plural = 'Entities'


class User(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=100)
    screen_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    profile_image_url = models.URLField()


class Tweet(models.Model):
    created_at = models.DateTimeField()
    tweet_id = models.IntegerField()
    text = models.TextField(max_length=300)
    source = models.CharField(max_length=300)
    in_reply_to_status_id = models.IntegerField()
    in_reply_to_user_id = models.IntegerField()
    in_reply_to_screen_name = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    category = models.IntegerField(choices=CATEGORY_CHOICES, null=True, blank=True)

    class Meta:
        ordering = ('-created_at',)
