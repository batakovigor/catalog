# Generated by Django 2.0.5 on 2018-05-15 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demowork', '0007_auto_20180515_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demoworks',
            name='tags',
            field=models.ManyToManyField(to='demowork.Tag', verbose_name='Тэги'),
        ),
    ]
