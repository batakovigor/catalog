from django.db.models import Q
import django_filters
import demowork.models
import itertools
from django import forms

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

def get_year_list():

    a = []
    b = []
    years = demowork.models.DemoWorks.objects.values('date_work__year').order_by('date_work__year').distinct()
    for y in years:
        a.append(y['date_work__year'])
        b.append(str(y['date_work__year']))

    YEAR_LIST = tuple(zip(a, b))

    return YEAR_LIST



def filter_not_empty(queryset, name, value):
    lookup = '__'.join([name, 'isnull'])
    return queryset.filter(**{lookup: False})


class DemoWorksFilter(django_filters.FilterSet):
    year_work = django_filters.ChoiceFilter(field_name='date_work__year', choices=get_year_list(), label='Год')
    month_work = django_filters.ChoiceFilter(field_name='date_work__month', choices=MONTH_LIST, label='Месяц')

    class Meta:
        model = demowork.models.DemoWorks

        # fields = {
        #     'id_otdel':['exact'],
        #     'date_work':['year__exact', 'month__exact'],
        # }
        #fields = ['id_otdel', 'year_work', 'month_work', 'm_work']
        fields = ['id_otdel', 'year_work', 'month_work']



class DemoWorksFilterEx(django_filters.FilterSet):
    ex = django_filters.CharFilter(label='Расширенный фильтр', method='filter_ex')
    search_fields = ['title', 'description', ]

    def filter_ex(self, qs, name, value):
        if value:
            q_parts = value.split()

            q_totals = Q()

            combinatorics = itertools.product([True, False], repeat=len(q_parts) - 1)

            possibilities = []

            for combination in combinatorics:
                i = 0
                one_such_combination = [q_parts[i]]
                for slab in combination:
                    i += 1
                    if not slab:  # there is a join
                        one_such_combination[-1] += ' ' + q_parts[i]
                    else:
                        one_such_combination += [q_parts[i]]
                possibilities.append(one_such_combination)

            for p in possibilities:
                list1 = self.search_fields
                list2 = p
                perms = [zip(x, list2) for x in itertools.permutations(list1, len(list2))]

                for perm in perms:
                    q_part = Q()
                    for p in perm:
                        q_part = q_part & Q(**{p[0] + '__icontains': p[1]})
                    q_totals = q_totals | q_part

            qs = qs.filter(q_totals)

        return qs

    class Meta:
        model = demowork.models.DemoWorks
        fields = ['ex']