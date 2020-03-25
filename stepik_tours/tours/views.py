from django.shortcuts import render
from django.views import View
from .data import tours

title = "Stepik Travel"
subtitle = "Для тех, кого отвлекают дома"
description = "Лучшие направления, где никто не будет вам мешать сидеть на берегу и изучать программирование, дизайн, разработку игр и управление продуктами"
departures = {"msk":"Из Москвы","spb":"Из Петербурга","nsk":"Из Новосибирска","ekb":"Из Екатеринбурга","kazan":"Из Казани"}

class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tours/index.html', context={'departures': departures, 'tours': tours})

class DepartureView(View):
    def count_props(self, departure="kzn"):
        min_price=tours[1]["price"]
        max_price=tours[1]["price"]
        min_stay=tours[1]["nights"]
        max_stay=tours[1]["nights"]
        for tour in tours:
            if tours[tour]["departure"] == departure:
                if tours[tour]["price"] < min_price:
                    min_price=tours[tour]["price"]
                elif tours[tour]["price"] > max_price:
                    max_price = tours[tour]["price"]
            if tours[tour]["departure"] == departure:
                if tours[tour]["nights"] < min_stay:
                    min_stay=tours[tour]["nights"]
                elif tours[tour]["nights"] > max_stay:
                    max_stay = tours[tour]["nights"]
        return {"min_price": min_price, "max_price": max_price, "min_stay": min_stay, "max_stay": max_stay}
    def get(self, request, departure="msk",  *args, **kwargs):
        return render(request, 'tours/departure.html', context={
                                                                    'destination': departures[departure],
                                                                    'departures': departures,
                                                                    'tours': tours,
                                                                    'properties': self.count_props()
        })