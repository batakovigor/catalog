import django_tables2 as tables
from django.utils.html import format_html
from django_tables2.utils import A  # alias for Accessor
from demowork.models import DemoWorks, RecordsDemoWorks


class DemoWorksTable(tables.Table):
    id_otdel = tables.LinkColumn('demowork_view', text=lambda record: record.id_otdel, args=[A('pk')])
    title = tables.LinkColumn('demowork_view', text=lambda record: record.title, args=[A('pk')])
    date_work = tables.LinkColumn('demowork_view', text=lambda record: record.date_work, args=[A('pk')])
    description = tables.LinkColumn('demowork_view', text=lambda record: record.description, args=[A('pk')])

    #chk = tables.TemplateColumn('<input type="checkbox" value="{{ record.pk }}" />', verbose_name="...")
    edit = tables.LinkColumn('demowork_edit', text=format_html('<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAACvSURBVDhP1dI7CsJQEIXhuwFxA27Dwvcr6B4EQezcna7FykpLH03UQjv9Z8wYRPBOGsEDH+QEJplLEv4qVaywRl1uFIkMnHDPbOBOAzucYQ/YwpUmZHiYXV9wxQDRyMAeibZ8k5G2SFqQYXuTDEt3DbdxQF/b+zGiseGutnwTO8bXyKc6oqPtc5Nolpg+L1/DPW2OlCE/SgUzyCZ2DFcmuCHFAjUUyhxjlLT9LiE8AMEBJiZWyGVOAAAAAElFTkSuQmCC">'), orderable=False, verbose_name="", args=[A('pk')])
    delete = tables.LinkColumn('demowork_delete', text=format_html('<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABLSURBVDhPY6AVaAXin0D8H0q3ADFJAKRJEMIE0yA+QQCyjViME+CVBAJC8nAFhGicYNSAwWAAcgpEB0SlSOQ8gI5B4k1APKgAAwMA0Fw/578RhNEAAAAASUVORK5CYII=">'), orderable=False, verbose_name="",  args=[A('pk')])


    class Meta:
        model = DemoWorks
        attrs = {
            'class': 'paleblue',
        }
        exclude = {'date_public','autor','tags','keywords'}
        template_name = 'django_tables2/bootstrap.html'


class RecordsDemoWorksTable(tables.Table):
    media = tables.FileColumn()

    edit = tables.LinkColumn('record_demowork_edit', text=format_html(
        '<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAACvSURBVDhP1dI7CsJQEIXhuwFxA27Dwvcr6B4EQezcna7FykpLH03UQjv9Z8wYRPBOGsEDH+QEJplLEv4qVaywRl1uFIkMnHDPbOBOAzucYQ/YwpUmZHiYXV9wxQDRyMAeibZ8k5G2SFqQYXuTDEt3DbdxQF/b+zGiseGutnwTO8bXyKc6oqPtc5Nolpg+L1/DPW2OlCE/SgUzyCZ2DFcmuCHFAjUUyhxjlLT9LiE8AMEBJiZWyGVOAAAAAElFTkSuQmCC">'),
                             orderable=False, verbose_name="", args=[A('pk')])
    delete = tables.LinkColumn('record_demowork_delete', text=format_html(
        '<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAABLSURBVDhPY6AVaAXin0D8H0q3ADFJAKRJEMIE0yA+QQCyjViME+CVBAJC8nAFhGicYNSAwWAAcgpEB0SlSOQ8gI5B4k1APKgAAwMA0Fw/578RhNEAAAAASUVORK5CYII=">'),
                               orderable=False, verbose_name="", args=[A('pk')])

    class Meta:
        model = RecordsDemoWorks
        attrs = {
            'class': 'paleblue',
        }
        exclude = {'id_demoworks','keywords'}
        template_name = 'django_tables2/bootstrap.html'