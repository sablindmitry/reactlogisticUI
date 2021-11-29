from django.forms import ModelForm, DateInput
from .models import Order
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from crispy_forms.bootstrap import FormActions

class DateInput(DateInput):
    input_type = 'date'


class OrderForm(ModelForm):
    class Meta:
        model = Order
        widgets = {'date': DateInput()}
        exclude = ['status', ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'order/'
        #self.helper.attrs = {'hx-post': 'order_ok/'}

        self.helper.layout = Layout(
            Row(
                Column('name'),
                Column('phone'),
                Column('email'),
            ),
            Row(
                Column('departure_from'),
                Column('arrival_to'),
            ),
            Row(
                Column('weight'),
                Column('height'),
                Column('capacity'),
                Column('date'),

            ),
            FormActions(
                Submit('save_order', 'Отправить заявку'),
            ),

        )
