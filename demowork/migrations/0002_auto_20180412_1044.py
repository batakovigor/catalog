# Generated by Django 2.0.4 on 2018-04-12 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demowork', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demoworks',
            name='date_work',
            field=models.DateField(verbose_name='Дата проведения работы'),
        ),
    ]