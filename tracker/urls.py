from django.urls import path
from .views import application_list, application_detail

urlpatterns = [
    path('', application_list, name='application_list'),
    path("<int:pk>/", application_detail, name="application_detail"),
]