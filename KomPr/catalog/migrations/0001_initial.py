# Generated by Django 4.2 on 2023-05-08 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LedDisplayModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название модуля', max_length=200)),
                ('manufacturer', models.CharField(help_text='Производитель', max_length=200)),
                ('operationEnvironment', models.CharField(blank=True, choices=[('i', 'Idoor'), ('o', 'Outdoor'), ('f', 'Flexible')], default='i', help_text='Рабочая среда', max_length=10)),
                ('pixelPitch', models.FloatField(help_text='Шаг пикселя')),
                ('width', models.IntegerField(help_text='Ширина модуля в мм.')),
                ('height', models.IntegerField(help_text='Высота модуля в мм.')),
                ('depth', models.FloatField(help_text='Глубина модуля в мм.')),
                ('horizontalViewingAngle', models.IntegerField(help_text='Горизонтальный угол обзора')),
                ('verticalViewingAngle', models.IntegerField(help_text='Вертикальный угол обзора')),
                ('bestViewingDistance', models.IntegerField(help_text='Лучшее расстояние для просмотра в м')),
                ('ledLamp', models.CharField(blank=True, help_text='Тип светодиода', max_length=20)),
                ('refreshFrequency', models.IntegerField(help_text='Частота обновления')),
                ('brightness', models.IntegerField(help_text='Яркость cd/㎡')),
                ('drivingMethod', models.CharField(blank=True, help_text='Режим сканирования', max_length=10)),
                ('lifeSpan', models.IntegerField(help_text='Срок службы в часах')),
                ('powerConsumption', models.IntegerField(help_text='Мощность модуля в Вт.')),
            ],
            options={
                'ordering': ['pixelPitch', 'operationEnvironment'],
            },
        ),
    ]
