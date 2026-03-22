from django.urls import path
from .views import application_list, application_detail, application_create, application_update

urlpatterns = [
    path('', application_list, name='application_list'),
    path("create/", application_create, name="application_create"),
    path("<int:pk>/", application_detail, name="application_detail"),
    path("<int:pk>/edit/", application_update, name="application_update"),
]