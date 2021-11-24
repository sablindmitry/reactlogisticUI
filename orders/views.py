from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_http_methods
from django.views.generic import FormView

from .forms import OrderForm


class OrderFormView(FormView):
    # template_name = 'order_form.html'
    form_class = OrderForm
    response_class = ['good']
    def form_valid(self, form):
       # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        messages.success(request, )
        # return super().form_valid(form)

# @require_http_methods(["GET", "POST"])
# def create_order(request):
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Заявка принята')
#     else:
#         form = OrderForm()
#     return render(request, 'order_form.html', {'form': form})
