from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import JobApplication
from .forms import JobApplicationForm

# Create your views here.
def application_list(request):
    selected_status = request.GET.get("status", "")
    search_query = request.GET.get("q", "")
    sort_by = request.GET.get("sort", "newest")
    applications = JobApplication.objects.all()

    if selected_status:
        applications = applications.filter(status=selected_status)

    if search_query:
        applications = applications.filter(company_name__icontains=search_query)

    total_count = JobApplication.objects.count()
    applied_count = JobApplication.objects.filter(status="Applied").count()
    interview_count = JobApplication.objects.filter(status="Interview").count()
    rejected_count = JobApplication.objects.filter(status="Rejected").count()
    offer_count = JobApplication.objects.filter(status="Offer").count()

    if sort_by == "newest":
        applications = applications.order_by("-date_applied")
    elif sort_by == "oldest":
        applications = applications.order_by("date_applied")
    elif sort_by == "company_asc":
        applications = applications.order_by("company_name")
    elif sort_by == "company_desc":
        applications = applications.order_by("-company_name")

    paginator = Paginator(applications, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "applications": applications,
        "selected_status": selected_status,
        "search_query": search_query,
        "total_count": total_count,
        "applied_count": applied_count,
        "interview_count": interview_count,
        "rejected_count": rejected_count,
        "offer_count": offer_count,
        "sort_by": sort_by,
        "page_obj": page_obj,
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