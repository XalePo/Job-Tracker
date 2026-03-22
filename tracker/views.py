from django.shortcuts import render, redirect
from .models import JobApplication
from .forms import JobApplicationForm

# Create your views here.
def application_list(request):
    selected_status = request.GET.get("status")
    applications = JobApplication.objects.all()

    if selected_status:
        applications = applications.filter(status=selected_status)

    context = {
        "applications": applications,
        "selected_status": selected_status,
    }

    return render(request, "tracker/application_list.html", context)


def application_detail(request, pk):
    application = JobApplication.objects.get(id=pk)
    context = {
        "application": application
    }

    return render(request, "tracker/application_detail.html", context)

def application_create(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("application_list")
    else:
        form = JobApplicationForm()
    
    context = {
        "form": form
    }

    return render(request, "tracker/application_form.html", context)

def application_update(request, pk):
    application = JobApplication.objects.get(id=pk)
    if request.method == "POST":
        form = JobApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect("application_detail", application.id)
    else:
        form = JobApplicationForm(instance=application)

    context = {
            "form": form
        }
    
    return render(request, "tracker/application_form.html", context)

def application_delete(request, pk):
    application = JobApplication.objects.get(id=pk)
    if request.method == "POST":
        application.delete()
        return redirect("application_list")
    
    context = {
        "application": application
    }    
    
    return render(request, "tracker/application_confirm_delete.html", context)