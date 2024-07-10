# newsletter/forms.py

from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Subscriber, Newsletter

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email', 'name']

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['title', 'content']
        widgets = {
            'content': SummernoteWidget(),  # Use SummernoteWidget for 'content' field
        }
