# Generated by Django 2.0.4 on 2018-04-12 05:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DemoWorks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование работы')),
                ('date_public', models.DateTimeField(auto_now=True, verbose_name='Дата публикации')),
                ('date_work', models.DateTimeField(verbose_name='Дата проведения работы')),
                ('keywords', models.CharField(max_length=100, verbose_name='Ключевые слова')),
                ('description', models.TextField(verbose_name='Описание работы')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Показательная работа',
                'verbose_name_plural': 'Показательные работы',
            },
        ),
        migrations.CreateModel(
            name='Otdel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование района')),
                ('short_name', models.CharField(max_length=10, verbose_name='Короткое наименование района')),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
            },
        ),
        migrations.CreateModel(
            name='RecordsDemoWorks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование файла влежения')),
                ('media', models.FilePathField(verbose_name='Путь расположения файла')),
                ('keywords', models.CharField(max_length=100, verbose_name='Ключевые слова')),
                ('description', models.TextField(verbose_name='Описание работы')),
                ('id_demoworks', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='demowork.DemoWorks', verbose_name='Наименование работы')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
        migrations.AddField(
            model_name='demoworks',
            name='id_otdel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='demowork.Otdel', verbose_name='Район'),
        ),
    ]
