# Generated by Django 2.0.6 on 2018-07-03 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0004_auto_20180702_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='status',
            field=models.IntegerField(choices=[('0', 'Не рассмотрено'), ('1', 'Рассмотрено'), ('2', 'Подходит'), ('3', 'Не подходит'), ('4', 'Отправлен тест'), ('5', 'Приглашен на интервью'), ('6', 'Интервью проведено'), ('7', 'Штат'), ('8', 'Резерв'), ('9', 'Стажёр'), ('10', 'Не прошел интервью')], default='0'),
        ),
    ]
