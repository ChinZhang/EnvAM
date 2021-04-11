from django.shortcuts import render

from . import helper
from .helper import return_graph, single_country_comp


def home(request):
    context = {'country_data1': helper.country_data(),
               'series_data1': helper.series_data(),
               'country_data2': helper.country_data(),
               'series_data2': helper.series_data(),
               'country_data3': helper.country_data(),
               'series_data3': helper.series_data(),
               'country_data4': helper.country_data(),
               'series_data4': helper.series_data(),
               }
    return render(request, 'home_page.html', context)


def test_graph(request):
    context = {'country_data1': helper.country_data(),
               'series_data1': helper.series_data(),
               'country_data2': helper.country_data(),
               'series_data2': helper.series_data(),
               'country_data3': helper.country_data(),
               'series_data3': helper.series_data(),
               'country_data4': helper.country_data(),
               'series_data4': helper.series_data(),
               }
    if request.method == 'POST':
        request.POST.get()
        context['graph'] = return_graph(single_country_comp(helper.data, 'AUS', 'CO2PC', 'GDPPUE'))
        return render(request, 'home_page.html', context)
    else:
        return render(request, 'home_page.html')

