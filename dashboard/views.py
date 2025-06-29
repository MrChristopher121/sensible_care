# dashboard/views.py 
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
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
# Active Clients
@login_required
def clients_view(request):
    # Page-level filters
    base_queryset = (
        Client.objects
            .exclude(Q(client_subgroup="HCP Brokerage") | Q(hcp_level_name="Other"))
            .filter(client_group="HCP", active_flag='Active')
            )
    
    # All records
    clients =  list(
        base_queryset.values(
            "client_id",
            "service_start_date",
            "client_group",
            "client_subgroup",
            "hcp_level_name",
            "state_code",
            "area",
            "case_managers"
            )
    )
    
    # Data for charts
    client_group_data = [
        list(row) for row in base_queryset
        .values_list("client_subgroup")
        .annotate(count=Count("client_id"))
        .values_list("client_subgroup", "count")
    ]

    hcp_level_data = [
        list(row) for row in base_queryset
        .values_list("hcp_level_name")
        .annotate(count=Count("client_id"))
        .values_list("hcp_level_name", "count")
    ]

    state_data = [
        list(row) for row in base_queryset
        .values_list("state_code")
        .annotate(count=Count("client_id"))
        .values_list("state_code", "count")
    ]

    return render(request, "clients/clients_active.html", {
            "clients": clients,
            "client_group_data": client_group_data,
            "hcp_level_data": hcp_level_data,
            "state_data": state_data
            })

# --------------------------------------------------------
# New Clients
@login_required
def clients_new_view(request):
    # Page-level filters
    base_queryset = (
        Client.objects
            .exclude(client_subgroup="HCP Brokerage")
            .filter(client_group="HCP", service_start_current_fytd =True)
            )
    
    # All records
    clients =  list(
        base_queryset.values(
            "client_id",
            "service_start_date",
            "client_group",
            "client_subgroup",
            "hcp_level_name",
            "state_code",
            "area",
            "case_managers"
            )
    )

    clients_fytd_data = [
        list(row) for row in base_queryset
        .values_list("client_group")
        .annotate(count=Count("client_id"))
        .values_list("client_group", "count")
    ]

    # Data for charts
    clients_state_data = [
        list(row) for row in base_queryset
        .values_list("state_code")
        .annotate(count=Count("client_id"))
        .values_list("state_code", "count")
    ]

    clients_group_data = [
        list(row) for row in base_queryset
        .values_list("client_subgroup")
        .annotate(count=Count("client_id"))
        .values_list("client_subgroup", "count")
    ]

    return render(request, "clients/clients_new.html", {
            "clients": clients,
            "clients_fytd_data": clients_fytd_data,
            "clients_state_data": clients_state_data,
            "clients_group_data": clients_group_data
            })


# --------------------------------------------------------
# Exited Clients
@login_required
def clients_exited_view(request):
    return render(request, "clients/clients_exited.html")

# --------------------------------------------------------
# Brokerage Clients
@login_required
def clients_brokerage_view(request):
    return render(request, "clients/clients_brokerage.html")

# --------------------------------------------------------
# Clients Using External Services
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

