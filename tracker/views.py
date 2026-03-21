from django.shortcuts import render
from .models import JobApplication

# Create your views here.
def application_list(request):
    applications = JobApplication.objects.all()
    context = {
        "applications": applications
    }

    return render(request, "tracker/application_list.html", context)


def application_detail(request, pk):
    application = JobApplication.objects.get(id=pk)
    context = {
        "application": application
    }

    return render(request, "tracker/application_detail.html", context)