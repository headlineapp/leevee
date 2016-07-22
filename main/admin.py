from django.contrib import admin
from models import User, UserMention, Entity, Tweet


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'location')


@admin.register(UserMention)
class UserMentionAdmin(admin.ModelAdmin):
    list_display = ('mention_id', 'screen_name')


@admin.register(Entity)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('tweet_id', 'text', 'created_at')