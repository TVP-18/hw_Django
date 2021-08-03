from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    file = settings.BUS_STATION_CSV

    with open(file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        station = []
        for el in reader:
            station.append({'Name': el['Name'], 'Street': el['Street'], 'District': el['District']})

    paginator = Paginator(station, 10)
    current_page = request.GET.get('page', 1)
    page = paginator.get_page(current_page)

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
