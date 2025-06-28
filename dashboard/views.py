# pages/views.py 
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Client

def home_page_view(request):
    context = {
        "greeting": "Thank you for visiting!", 
    }
    return render(request, "main/home.html", context)

def about_page_view(request):
    context = {
        "contact_address": "Melbourne, Australia", 
        "phone_number": "555-555-5555"
    }
    return render(request, "main/about.html", context)


# --------------------------------------------------------
@login_required
# Clients Dashboard
def clients_view(request):
    clients = Client.objects.filter(client_group='HCP')

    # Create paginator with 20 rows per page
    paginator = Paginator(clients, 20) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'clients/clients_active.html', {
        'page_obj': page_obj}
        )
    #return render(request, "clients/clients_active.html", {'clients': clients})

@login_required
def clients_new_view(request):
    return render(request, "clients/clients_new.html")

@login_required
def clients_exited_view(request):
    return render(request, "clients/clients_exited.html")

@login_required
def clients_brokerage_view(request):
    return render(request, "clients/clients_brokerage.html")

@login_required
def clients_external_services_view(request):
    return render(request, "clients/clients_external_services.html")


# --------------------------------------------------------
# Employees Dashboard
@login_required
def employee_view(request):
    return render(request, "employees/employees.html")


# --------------------------------------------------------
# Service Hours Dashboard
@login_required
def service_view(request):
    return render(request, "services/services.html")


# --------------------------------------------------------
# Travel Dashboard
@login_required
def travel_view(request):
    return render(request, "travel/travel.html")


# --------------------------------------------------------
# Case Manager 
@login_required
def case_manager_view(request):
    return render(request, "case_manager/case_manager.html")

