from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/lausstorf
    path('', views.index, name="job_offers-index"),
    path('<int:id>', views.get_job_offer_by_id, name="job_offers-detail"),
]