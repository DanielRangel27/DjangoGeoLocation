from django.shortcuts import render
from django.views.generic import View
from .utils import yelp_search, get_client_data

class IndexView(View):
    def get(self, reguest, *args, **kwargs):
        itens = []
        city = None

        while not city:
            ret = get_client_data()
            if ret:
                city = ret['city']

        q =reguest.GET.get('key', None)
        loc = reguest.GET.get('loc', None)
        location = city

        context = {
            'city' : city,
            'busca' : False
        }

        if loc:
            location = loc
        if q:
            itens = yelp_search(keyword=q, location=location)
            context = {
                'itens': itens,
                'city' : location,
                'busca': True
            }
        return render(reguest, 'index.html', context)