from django import forms
from django.forms import ModelForm

from .models import DemoWorks, RecordsDemoWorks


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