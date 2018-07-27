from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Otdel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование района')
    short_name = models.CharField(max_length=10, verbose_name='Короткое наименование района')

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'
        ordering = ['title']


    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тэг')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.title

class DemoWorks(models.Model):
    id_otdel = models.ForeignKey(Otdel, on_delete=models.PROTECT, verbose_name='Район')
    title = models.CharField(max_length=100, verbose_name='Наименование работы')
    date_public = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    date_work = models.DateField(verbose_name='Дата проведения работы')
    autor = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')
    tags = models.ManyToManyField(Tag, verbose_name='Тэги')
    keywords = models.CharField(max_length=100, verbose_name='Ключевые слова',null=True)
    description = models.TextField(verbose_name='Описание работы')

    class Meta:
        verbose_name = 'Показательная работа'
        verbose_name_plural = 'Показательные работы'

    def __str__(self):
        return self.title


class RecordsDemoWorks(models.Model):
    id_demoworks = models.ForeignKey(DemoWorks, on_delete=models.PROTECT,verbose_name='Наименование работы')
    title = models.CharField(max_length=100, verbose_name='Наименование файла влежения')
    media = models.FileField('Файлы', upload_to='demowork/media', default='', blank=True)
    keywords = models.CharField(max_length=100, verbose_name='Ключевые слова')
    description = models.TextField(verbose_name='Описание работы')

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def __str__(self):
        return self.title

