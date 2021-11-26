from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
from .forms import EmailSignupForm
from .models import SignUp

from django.shortcuts import render
from django.contrib import messages

from django.conf import settings
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError

import json
import requests

api_key = settings.MAILCHIMP_API_KEY
server = settings.MAILCHIMP_DATA_CENTER
list_id = settings.MAILCHIMP_EMAIL_LIST_ID

from django.shortcuts import render
from django.contrib import messages



# Create your views here.

# Subscription Logic
def subscribe(email):

    mailchimp = Client()
    mailchimp.set_config({
        "api_key": api_key,
        "server": server,
    })

    member_info = {
        "email_address": email,
        "status": "subscribed",
    }

    try:
        response = mailchimp.lists.add_list_member(list_id, member_info)
        print("response: {}".format(response))
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))




# Views here.
# def subscription(request):
#     if request.method == "POST":
#         email = request.POST['email']
#         subscribe(email)                    # function to access mailchimp
#         print(email)
#         messages.success(request, "Email reçu. Merci! ") # message

#     return redirect('home')

def subscription(request):
    form = EmailSignupForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            email_signup_qs = SignUp.objects.filter(email=form.instance.email)
            if email_signup_qs.exists():
                messages.warning(request, "Vous avez déjà souscrit(e) à la newsletter")
            else:
                subscribe(form.instance.email)
                messages.info(request, "Merci d'avoir souscrit(e) à la newsletter")

                form.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
