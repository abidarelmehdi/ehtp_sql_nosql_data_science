from django.urls import path
from .views import Index, SignUp

app_name = "ehtp"
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('signup/', SignUp.as_view(), name='signup')
]
