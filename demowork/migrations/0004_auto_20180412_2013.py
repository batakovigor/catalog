# Generated by Django 2.0.4 on 2018-04-12 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demowork', '0003_auto_20180412_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demoworks',
            name='date_public',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
    ]