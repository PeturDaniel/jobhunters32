from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/vinnustadir
    path('', views.index, name="employers-index"),
    path('<int:id>', views.get_employer_by_id, name="employer-detail"),
]
