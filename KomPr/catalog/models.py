from django.db import models

# Create your models here.

class LedDisplayModule(models.Model):
    name = models.CharField(max_length=200, help_text="Название модуля")
    manufacturer = models.CharField(max_length=200, help_text="Производитель")
    ENVIRONMENT_STATUS = (
        ('i', 'Indoor'),
        ('o', 'Outdoor'),
        ('f', 'Flexible'),
    )
    operationEnvironment = models.CharField(max_length=10, choices=ENVIRONMENT_STATUS, blank=True, default='i', help_text='Рабочая среда')
    pixelPitch = models.FloatField(help_text='Шаг пикселя')
    width = models.IntegerField(help_text='Ширина модуля в мм.')
    height = models.IntegerField(help_text='Высота модуля в мм.')
    depth = models.FloatField(help_text='Глубина модуля в мм.')
    horizontalViewingAngle = models.IntegerField(help_text='Горизонтальный угол обзора')
    verticalViewingAngle = models.IntegerField(help_text='Вертикальный угол обзора')
    bestViewingDistance = models.IntegerField(help_text='Лучшее расстояние для просмотра в м')
    ledLamp = models.CharField(max_length=20, blank=True, help_text='Тип светодиода')
    refreshFrequency = models.IntegerField(help_text='Частота обновления')
    brightness = models.IntegerField(help_text='Яркость cd/㎡')
    drivingMethod = models.CharField(max_length=10, blank=True, help_text='Режим сканирования')
    lifeSpan = models.IntegerField(help_text='Срок службы в часах')
    powerConsumption = models.IntegerField(help_text='Мощность модуля в Вт.')


    def __str__(self):
        return self.name

    class Meta:
        ordering = ["pixelPitch", "operationEnvironment"]