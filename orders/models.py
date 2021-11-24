from django.db import models

# Create your models here.

ORDER_STATUS = [
    (1 ,'Получен'),
    (2, 'Принят'),
    (3, 'Выполнен'),
    (4 , 'Отменен'),
]

class Order(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')
    departure_from = models.CharField(max_length=150,verbose_name='Откуда')
    arrival_to = models.CharField(max_length=150, verbose_name='Куда')
    weight = models.IntegerField(verbose_name='Вес')
    capacity = models.IntegerField(verbose_name='Объем')
    height = models.IntegerField(verbose_name='Высота')
    date = models.DateTimeField(verbose_name='Желаемая дата')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=150, choices=ORDER_STATUS, null=True, blank=True)
