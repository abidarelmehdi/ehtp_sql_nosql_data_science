from django.urls import path
from .views import Index, SignUp, get_ip_info

app_name = 'ehtp'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('accounts/signup/', SignUp.as_view(), name='signup'),
    path('api/ip_info/', get_ip_info, name='client_ip_info')
]
