from django.shortcuts import render
from .models import JobApplication

# Create your views here.
def application_list(request):
    applications = JobApplication.objects.all()
    context = {
        "applications": applications
    }

    return render(request, "tracker/application_list.html", context)