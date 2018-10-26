from django.http import FileResponse, Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import ListView
from django_tables2 import RequestConfig, SingleTableView
from django.views.generic.edit import FormView
from .filters import DemoWorksFilter, DemoWorksFilterEx
from .forms import DemoWorksForm, FileFieldForm
from .models import DemoWorks, RecordsDemoWorks
from .tables import DemoWorksTable, RecordsDemoWorksTable


# Create your views here.

def get_month(month):
    month_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
                  'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    return month_list[int(month-1)]

def get_date(date):
    day_list = ['первое', 'второе', 'третье', 'четвёртое',
        'пятое', 'шестое', 'седьмое', 'восьмое',
        'девятое', 'десятое', 'одиннадцатое', 'двенадцатое',
        'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
        'семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое',
        'двадцать первое', 'двадцать второе', 'двадцать третье',
        'двадацать четвёртое', 'двадцать пятое', 'двадцать шестое',
        'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое',
        'тридцатое', 'тридцать первое']
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
           'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    date_list = date.split('.')
    return (day_list[int(date_list[0]) - 1] + ' ' +
        month_list[int(date_list[1]) - 1] + ' ' +
        date_list[2] + ' года')



class FilteredSingleTableView(SingleTableView):
    filter_class = None

    def get_table_data(self):
        data = super(FilteredSingleTableView, self).get_table_data()
        self.filter = self.filter_class(self.request.GET, queryset=data)
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super(FilteredSingleTableView, self).get_context_data(**kwargs)
        context['filter'] = self.filter
        return context

class DemoWorksFilteredSingleTableView(FilteredSingleTableView):
    model = DemoWorks
    table_class = DemoWorksTable
    filter_class = DemoWorksFilter

class DemoWorksSingleTableView(SingleTableView):
    model = DemoWorks
    table_class = DemoWorksTable

class FilteredTableView(ListView):
    model = DemoWorks

    def get_context_data(self, **kwargs):
        context = super(FilteredTableView, self).get_context_data(**kwargs)
        filter = DemoWorksFilter(self.request.GET, queryset=self.object_list)

        table = DemoWorksTable(filter.qs)
        RequestConfig(self.request, ).configure(table)

        context['filter'] = filter
        context['table'] = table
        return context


class FilterExListView(ListView):
    model = DemoWorks

    def get_context_data(self, **kwargs):
        context = super(FilterExListView, self).get_context_data(**kwargs)
        filter = DemoWorksFilterEx(self.request.GET, queryset=self.object_list)

        table = DemoWorksTable(filter.qs)
        RequestConfig(self.request, ).configure(table)

        context['filter'] = filter
        context['table'] = table

        return context

def pdf_view(request, file_pdf):
    try:
        return FileResponse(open(file_pdf, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'demowork/demoworks_upload_files.html' # Replace with your template.
    success_url = '...' # Replace with your URL or reverse().
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                pass
            return self.form_valid(form)
        else:
            pass

        return self.form_invalid(form)

def DemoWorksView(request, pk):
    template_name = 'demowork/demoworks_detail.html'
    #w_list = DemoWorks.objects.filter(date_public__year=year, date_public__month=month, pk=pk)

    demowork = get_object_or_404(DemoWorks, pk=pk)
    form_demowork = DemoWorksForm(request.POST or None, instance=demowork)

    table = RecordsDemoWorksTable(RecordsDemoWorks.objects.filter(id_demoworks = pk))
    RequestConfig(request).configure(table)

    context = {
        'form_demowork': form_demowork,
        'table': table
    }
    return render(request, template_name, context)

def DemoWorksSave(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            demowork = DemoWorksTable(DemoWorks.objects.all())
            RequestConfig(request, ).configure(demowork)
            data['html_demowork_list'] = render_to_string('demowork/demoworks_list_update.html', {'table': demowork},
                                                           request=request)
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def DemoWorksCreate(request):
    template_name = 'demowork/includes/partial_demowork_create.html'
    if request.method == 'POST':
        form = DemoWorksForm(request.POST)
    else:
        form = DemoWorksForm()

    return DemoWorksSave(request, form, template_name)

#,
def DemoWorksUpdate(request, pk):
    template_name = 'demowork/includes/partial_demowork_update.html'
    demowork = get_object_or_404(DemoWorks, pk=pk)
    if request.method == 'POST':
        form = DemoWorksForm(request.POST, instance=demowork)
        table = RecordsDemoWorksTable(RecordsDemoWorks.objects.filter(id_demoworks=pk))
        RequestConfig(request).configure(table)
        context = {'form': form, 'table': table}
    else:
        form = DemoWorksForm(instance=demowork)
    return DemoWorksSave(request, form, template_name)

    #context = {'form': form, 'table': table}
    #html_form = render_to_string(template_name, context, request=request)
    #return JsonResponse({'html_form': html_form})

def DemoWorksDelete(request, pk):
    template_name = 'demowork/includes/partial_demowork_delete.html'
    demowork = get_object_or_404(DemoWorks, pk=pk)
    data = dict()
    if request.method == 'POST':
        demowork.delete()
        data['form_is_valid'] = True
        table = DemoWorksTable(DemoWorks.objects.all())
        RequestConfig(request, ).configure(table)
        data['html_demowork_list'] = render_to_string('demowork/demoworks_list_update.html', {'table': table},
                                                       request=request)
    else:
        context = {'demowork': demowork}
        data['html_form'] = render_to_string(template_name, context, request=request)

    return JsonResponse(data)

def RecordDemoWorksUpdate(request, pk):
    pass

def RecordDemoWorksDelete(request, pk):
    pass

def RecordDemoWorksCreate(request):
    pass

def RecordDemoWorksView(request, pk):
    pass