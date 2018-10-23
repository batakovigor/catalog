from django import forms
from django.forms import ModelForm

from .models import DemoWorks, RecordsDemoWorks, Otdel


class DemoWorksForm(ModelForm):
    class Meta:
        model = DemoWorks
        fields = ['id_otdel', 'title', 'date_work', 'tags', 'keywords', 'description']

class RecordsDemoWorksForm(ModelForm):
    class Meta:
        model = RecordsDemoWorks
        fields = ['id_demoworks', 'title', 'media', 'keywords', 'description']

class FileFieldForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class UserForm(forms.Form):
    pass

class FilterForm(forms.Form):
    MONTH_LIST = (
        (1, 'январь'),
        (2, 'февраль'),
        (3, 'март'),
        (4, 'апрель'),
        (5, 'май'),
        (6, 'июнь'),
        (7, 'июль'),
        (8, 'август'),
        (9, 'сентябрь'),
        (10, 'октябрь'),
        (11, 'ноябрь'),
        (12, 'декабрь'),
    )

    otdel = forms.ChoiceField(choices=Otdel.objects.all())
    year_work = forms.ChoiceField(choices=[('2015', '2015'),('2018', '2018')])
    month_work = forms.ChoiceField(choices=MONTH_LIST)

    def __init__(self, *args, **kwargs):
        super().__iter__(*args, **kwargs)
