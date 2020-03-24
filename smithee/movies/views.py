from django.conf import settings
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, Http404, HttpResponseNotFound


movies = [
    {
        'title': 'Catchfire',
        'year': 1990,
    },
    {
        'title': 'Mighty Ducks the Movie: The First Face-Off',
        'year': 1997,
    },
    {
        'title': 'Le Zombi de Cap-Rouge',
        'year': 1997,
    },
]


class MovieView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'movies/index.html', context={
                'director': settings.DIRECTOR,
                'movies': movies,
            }
        )

class ProducerView(View):
    def get(self, request, year=1979):
        return HttpResponse(f'Producer {year}')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините!')