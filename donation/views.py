from django.shortcuts import render
import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()
# Create your views here.
import stripe
stripe.api_key = env('STRIPE_SECRET_KEY')


def donationPage(request):
    return render(request, 'donation/donation.html', {'title': 'Stripe'})