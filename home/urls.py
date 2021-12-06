from django.urls import path
from .views import homedisplay, banks

urlpatterns = [
    path('', homedisplay, name='homesite1'),
    path('banks', banks, name='banks'),
]
