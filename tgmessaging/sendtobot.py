import datetime
from django.conf import settings
import httpx
import json

url = settings.TG_URL
token = settings.TG_TOKEN
method = settings.TG_METHOD
chat_id = settings.TG_CHAT_ID

# token = '2146445434:AAEn6vkyEEp0oeiwx3u3piD6pMxc6FRialE'
# url = f'https://api.telegram.org/bot{token}/'
# method = 'sendMessage'
# chat_id = '338540940'
def defaultconventer(o):
    if isinstance(o, datetime.date):
        return o.__str__()

#{'name': 'Dmitry Sablin', 'phone': '+79176283639', 'email': 'sablind1981@gmail.com', 'departure_from': 'w', 'arrival_to': 'we', 'weight': 79, 'capacity': 1, 'height': 172, 'date': datetime.datetime(2021, 11, 20, 0, 0, tzinfo=<UTC>)}


def send_order_to_tg(url, method, chat_id, data):
    phone = (str('%2b'+data.get("phone"))).replace(' ','').replace('+','')
    text = f'Полученая новая заявка :%0A Имя:  {data.get("name")} %0A тел:{phone}   %0A Из {data.get("departure_from")} в {data.get("arrival_to")} %0A на {data.get("date").day}.{data.get("date").month}.{data.get("date").year} %0A Проверьте почту sablind@mail.ru'
    return httpx.post(f'{url}{method}?chat_id={chat_id}&text={text}')


