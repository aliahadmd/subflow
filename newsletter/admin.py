# admin.py

from django.contrib import admin
from newsletter.models import Subscriber, Newsletter, SentNewsletter

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_active', 'date_subscribed')
    list_filter = ('is_active', 'date_subscribed')
    search_fields = ('email', 'name')

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at', 'is_draft')
    list_filter = ('is_draft', 'author')
    search_fields = ('title', 'content')

@admin.register(SentNewsletter)
class SentNewsletterAdmin(admin.ModelAdmin):
    list_display = ('newsletter', 'subscriber', 'sent_at', 'is_opened', 'opened_at')
    list_filter = ('is_opened', 'sent_at')
    search_fields = ('newsletter__title', 'subscriber__email')