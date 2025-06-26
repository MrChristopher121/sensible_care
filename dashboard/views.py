# pages/views.py 
from django.shortcuts import render

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
# Clients Dashboard
def clients_view(request):
    return render(request, "clients/clients_active.html")

def clients_new_view(request):
    return render(request, "clients/clients_new.html")

def clients_exited_view(request):
    return render(request, "clients/clients_exited.html")

def clients_brokerage_view(request):
    return render(request, "clients/clients_brokerage.html")

def clients_external_services_view(request):
    return render(request, "clients/clients_external_services.html")


# --------------------------------------------------------
# Employees Dashboard
def employee_view(request):
    return render(request, "employees/employees.html")


# --------------------------------------------------------
# Service Hours Dashboard
def service_view(request):
    return render(request, "services/services.html")


# --------------------------------------------------------
# Travel Dashboard
def travel_view(request):
    return render(request, "travel/travel.html")


# --------------------------------------------------------
# Case Manager 
def case_manager_view(request):
    return render(request, "case_manager/case_manager.html")
