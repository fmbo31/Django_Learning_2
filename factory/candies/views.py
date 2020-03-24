from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views import View

class MainPageView(View):
    def get(self, request, *args, **kwargs):

        html =  "\n".join(f"<div>{candy}</div>" for candy in candies)
        return HttpResponse(html)

class CandyView(View):
    def get(self, request, candy_name, *args, **kwargs):
        if candy_name not in candies:
            raise Http404

        candy_info = "".join(
            f"<tr><td>{key}:</td><td>{value}</td></tr>"
            for key, value in candies[candy_name].items()
        )
        return HttpResponse(f"<table><tbody>{candy_info}</tbody></table>")

candies = {
    "Fudge":  {
        "color": "beige",
        "price": "priceless",
        "available": 100,
    },
    "Chocolate shock": {
        "color": "brown",
        "price": "precious",
        "available": 50,
    },
    "Marshmallow" : {
        "color": "pink",
        "price": "all the money in the world",
        "available": 200,
    },
}