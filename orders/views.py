from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_http_methods
from django.views.generic import FormView
from tgmessaging.sendtobot import send_order_to_tg, url, method, chat_id
from .forms import OrderForm


class OrderFormView(FormView):
    form_class = OrderForm
    #response_class = ['good']
    success_url = '/'
    def form_valid(self, form):
       # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print(form.cleaned_data)
        send_order_to_tg(url, method, chat_id, form.cleaned_data)
        form.save()
        return super().form_valid(form)
