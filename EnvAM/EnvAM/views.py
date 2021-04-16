from django.shortcuts import render

from . import helper
from .helper import return_graph, single_country_comp


def home(request):
    context = {'country_data': helper.country_data().items(),
               'series_data': helper.series_data().items(),
               }
    return render(request, 'home_page.html', context)


def test_graph(request):
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

        context['graph'] = return_graph(df)
        context['r_value'] = helper.corr_coef(df)
        context['country_name'] = cdata[country_code]
        context['series_name1'] = sdata[data_one]
        context['series_name2'] = sdata[data_two]

        return render(request, 'home_page.html', context)
    else:
        return render(request, 'home_page.html', context)

