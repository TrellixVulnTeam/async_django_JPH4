from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView
from django.views import View
from django.http import JsonResponse
from django.contrib import messages
from .models import Product
import json
import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()
import stripe
# This is your test secret API key.
stripe.api_key = env.get_value('STRIPE_SECRET_KEY')




class CreateIntent(View):
    
    def post(self, request, *args, **kwargs):
        try:
            amt = Product.objects.get(id=1).price
            print(amt)
            # my_product = Product.objects.all()[0]
            # print(my_product)
            # data = json.loads(request.data)
            intent = stripe.PaymentIntent.create(
                amount=amt,
                currency='usd'
            )

            return JsonResponse({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            print(e)
            return JsonResponse({'error': str(e)})
       
        
    # if request.method == 'POST':
    #     print('data:', request.POST)
    #     return redirect('playground')
        
    # return render(request, 'stripe_testing/donate.html', {'title': 'Stripe Testing', 'client_secret': intent.client_secret, 'intent': intent})

def ProductView(request):
    return render(request, 'stripe_testing/product_page.html')

def Donate(request):
    return render(request, 'stripe_testing/donate.html')


def Charge(request):
    checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1KmPv7KwrmecwB31BorpDxJ7',
                    'quantity': 1,
                },
                 {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1KmZ8lKwrmecwB31QblzRagw',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url= 'http://127.0.0.1:8000/',
            cancel_url= 'http://127.0.0.1:8000/',
        )
    
    return redirect(checkout_session.url)