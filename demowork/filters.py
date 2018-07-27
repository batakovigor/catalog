from django.db.models import Q
import django_filters
import demowork.models
import itertools
from django import forms

def filter_not_empty(queryset, name, value):
    lookup = '__'.join([name, 'isnull'])
    return queryset.filter(**{lookup: False})


class DemoWorksFilter(django_filters.FilterSet):
    year_work = django_filters.NumberFilter(field_name='date_work', lookup_expr='year', label='Год')
    month_work = django_filters.NumberFilter(field_name='date_work', lookup_expr='month', label='Месяц')
    #m_work = django_filters.ModelChoiceFilter(queryset=demowork.models.DemoWorks.objects.filter(date_work__month__in=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']))
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