from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/lausstorf
    path('', views.index, name="job_offers-index"),
]