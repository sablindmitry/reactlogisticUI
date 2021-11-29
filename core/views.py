from django.shortcuts import render

# Create your views here.
from orders.forms import OrderForm


def index(request):
    form = OrderForm()
    return render(request, 'base.html', {'form': form})

def order_ok(request):
    return render(request, 'core/ok.html')