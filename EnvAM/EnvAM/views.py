from django.shortcuts import render

from . import helper
from .helper import return_graph, single_country_comp, find_correlation_all_years, find_correlation_all_countries


def home(request):
    context = {'country_data': helper.country_data().items(),
               'series_data': helper.series_data().items(),
               }
    return render(request, 'home_page.html', context)


def compare_per_country_graph(request):
    cdata = helper.country_data()
    sdata = helper.series_data()
    context = {'country_data': cdata.items(),
               'series_data': sdata.items(),
               }
    if request.method == 'POST':
        data_one = request.POST.get("scode1")
        data_two = request.POST.get("scode2")
        country_code = request.POST.get("ccode")
        df = single_country_comp(helper.data, country_code, data_one, data_two)

        context['compare_per_country_graph'] = return_graph(df)
        context['r_value'] = "R-value: " + helper.corr_coef(df)
        context['country_name'] = cdata[country_code]
        context['series_name1'] = "x-axis: " + sdata[data_one]
        context['series_name2'] = "y-axis: " + sdata[data_two]

        return render(request, 'home_page.html', context)
    else:
        return render(request, 'home_page.html', context)


def correlation_range(request):
    cdata = helper.country_data()
    sdata = helper.series_data()
    context = {'country_data': cdata.items(),
               'series_data': sdata.items(),
               }

    if request.method == 'POST':
        data_one = request.POST.get("scode1")
        data_two = request.POST.get("scode2")
        corr_coef = request.POST.get("range")

        context['list_of_correlations'] = find_correlation_all_countries(helper.data, data_one, data_two, corr_coef).items()
        context['series_name1_range'] = "Data 1: " + sdata[data_one]
        context['series_name2_range'] = "Data 2: " + sdata[data_two]
        context['r_value_range'] = "Range: " + "x > " + corr_coef + " and x < -" + corr_coef

        return render(request, 'home_page.html', context)
    else:
        return render(request, 'home_page.html', context)


def compare_years_graph(request):
    sdata = helper.series_data()
    cdata = helper.country_data()
    context = {'series_data': sdata.items(),
               'country_data': cdata.items(),
               }

    if request.method == 'POST':
        data_one = request.POST.get("scode1")
        data_two = request.POST.get("scode2")

        context['compare_correlation_all_years_graph'] = find_correlation_all_years(helper.data, data_one, data_two)
        context['series_name1_years'] = "Data 1: " + sdata[data_one]
        context['series_name2_years'] = "Data 2: " + sdata[data_two]

        return render(request, 'home_page.html', context)
    else:
        return render(request, 'home_page.html', context)