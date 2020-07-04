from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Subscribe
from .forms import SubscribeForm
import requests
import json
from django.conf import settings
from django.http import HttpResponseRedirect


def contact(request):
    if request.method == 'POST':
        full_name = request.POST['fullname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            email,
            ['jameskulu55@gmail.com'],
            fail_silently=True,
        )
        messages.success(request, 'Your message has been sent successfully.')
        return redirect('contact')

    return render(request, 'Contact/contact.html')


MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_AUDIENCE_ID = settings.MAILCHIMP_EMAIL_AUDIENCE_ID

api_url = 'https://{dc}.api.mailchimp.com/3.0'.format(dc=MAILCHIMP_DATA_CENTER)
members_endpoint = '{api_url}/lists/{list_id}/members'.format(
    api_url=api_url,
    list_id=MAILCHIMP_EMAIL_AUDIENCE_ID
)


def subscribe(email):
    data = {
        "email_address": email,
        "status": "subscribed"
    }
    r = requests.post(
        members_endpoint,
        auth=("", MAILCHIMP_API_KEY),
        data=json.dumps(data)
    )
    return r.status_code, r.json()


def email_list_signup(request):
    form = SubscribeForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            email_signup_qs = Subscribe.objects.filter(
                email=form.instance.email)
            if email_signup_qs.exists():
                messages.success(
                    request, "You are already subscribed to our newsletter.")
            else:
                subscribe(form.instance.email)
                form.save()
                messages.success(
                    request, "You have successfully subscribed to our newsletter.")
                return redirect('home')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
