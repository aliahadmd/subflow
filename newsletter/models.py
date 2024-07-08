# models.py

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.crypto import get_random_string

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)
    unsubscribe_token = models.CharField(max_length=32, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.unsubscribe_token:
            self.unsubscribe_token = get_random_string(32)
        super().save(*args, **kwargs)

    def get_unsubscribe_url(self):
        return reverse('unsubscribe', kwargs={'token': self.unsubscribe_token})

    def __str__(self):
        return self.email
    

class Newsletter(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class SentNewsletter(models.Model):
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)
    is_opened = models.BooleanField(default=False)
    opened_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('newsletter', 'subscriber')

    def __str__(self):
        return f"{self.newsletter.title} - {self.subscriber.email}"
