from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.http import JsonResponse

from geoip2 import database as geoip
from geoip2.errors import AddressNotFoundError
from ipware import get_client_ip

from time import sleep


class Index(LoginRequiredMixin, TemplateView):
    template_name = 'ehtp/index.html'


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def get_ip_info(request):
    client_ip, is_routable = get_client_ip(request)
    data = {
        'ip': client_ip,
        'status': 405
    }
    if is_routable:
        try:
            maxmind_responce = geoip.Reader(
                settings.MAXMIND_DB_FILE
            ).city(client_ip)
            data.update({
                'continent': maxmind_responce.continent.name,
                'country': maxmind_responce.country.name,
                'city': maxmind_responce.city.name,
                'latitude': maxmind_responce.location.latitude,
                'longitude': maxmind_responce.location.longitude,
                'status': 200
            })
        except AddressNotFoundError:
            data.update({'status': 404})

    sleep(5)
    return JsonResponse(data)
