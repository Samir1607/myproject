from django.urls import path
from .views import homepage, paymenthandler


urlpatterns = [
    path('', homepage, name='index'),
    path('paymenthandler/', paymenthandler, name='paymenthandler'),
]
