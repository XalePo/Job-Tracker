from django.urls import path
from .views import application_list, application_detail, application_create

urlpatterns = [
    path('', application_list, name='application_list'),
    path("create/", application_create, name="application_create"),
    path("<int:pk>/", application_detail, name="application_detail"),
]