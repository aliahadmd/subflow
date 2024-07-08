# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Subscriber, Newsletter, SentNewsletter
from .forms import SubscriberForm, NewsletterForm
from django.core.mail import send_mass_mail
from django.conf import settings
from django.utils import timezone
from django.db import IntegrityError
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

def home(request):
    return render(request, 'newsletter/home.html')

def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully subscribed!')
            return redirect('home')
    else:
        form = SubscriberForm()
    return render(request, 'newsletter/subscribe.html', {'form': form})

@login_required
def newsletter_list(request):
    newsletters = Newsletter.objects.filter(author=request.user)
    return render(request, 'newsletter/newsletter_list.html', {'newsletters': newsletters})

@login_required
def newsletter_create(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            newsletter = form.save(commit=False)
            newsletter.author = request.user
            newsletter.save()
            messages.success(request, 'Newsletter created successfully!')
            return redirect('newsletter_list')
    else:
        form = NewsletterForm()
    return render(request, 'newsletter/newsletter_form.html', {'form': form})

@login_required
def newsletter_edit(request, pk):
    newsletter = get_object_or_404(Newsletter, pk=pk, author=request.user)
    if request.method == 'POST':
        form = NewsletterForm(request.POST, instance=newsletter)
        if form.is_valid():
            form.save()
            messages.success(request, 'Newsletter updated successfully!')
            return redirect('newsletter_list')
    else:
        form = NewsletterForm(instance=newsletter)
    return render(request, 'newsletter/newsletter_form.html', {'form': form})

@login_required
def newsletter_delete(request, pk):
    newsletter = get_object_or_404(Newsletter, pk=pk, author=request.user)
    if request.method == 'POST':
        newsletter.delete()
        messages.success(request, 'Newsletter deleted successfully!')
        return redirect('newsletter_list')
    return render(request, 'newsletter/newsletter_confirm_delete.html', {'newsletter': newsletter})


def unsubscribe(request, token):
    subscriber = get_object_or_404(Subscriber, unsubscribe_token=token)
    if request.method == 'POST':
        subscriber.is_active = False
        subscriber.save()
        messages.success(request, 'You have been unsubscribed successfully.')
        return redirect('home')
    return render(request, 'newsletter/unsubscribe_confirm.html', {'subscriber': subscriber})



@login_required
def send_newsletter(request, pk):
    newsletter = get_object_or_404(Newsletter, pk=pk, author=request.user)
    if request.method == 'POST':
        subscribers = Subscriber.objects.filter(is_active=True)
        
        for subscriber in subscribers:
            subject = newsletter.title
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = subscriber.email

            context = {
                'subscriber': subscriber,
                'newsletter': newsletter,
                'unsubscribe_url': request.build_absolute_uri(subscriber.get_unsubscribe_url()),
            }

            # Render HTML content
            html_content = render_to_string('newsletter/email_template.html', context)
            
            # Create plain text content
            text_content = strip_tags(html_content)

            # Create the email message
            email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
            email.attach_alternative(html_content, "text/html")
            
            # Send the email
            email.send()

            try:
                SentNewsletter.objects.create(
                    newsletter=newsletter,
                    subscriber=subscriber,
                    sent_at=timezone.now()
                )
            except IntegrityError:
                sent_newsletter = SentNewsletter.objects.get(
                    newsletter=newsletter,
                    subscriber=subscriber
                )
                sent_newsletter.sent_at = timezone.now()
                sent_newsletter.save()
        
        newsletter.is_draft = False
        newsletter.save()
        
        messages.success(request, 'Newsletter sent successfully!')
        return redirect('newsletter_list')
    return render(request, 'newsletter/send_newsletter_confirm.html', {'newsletter': newsletter})