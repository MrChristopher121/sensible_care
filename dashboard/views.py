# dashboard/views.py 
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Count
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
# Clients Dashboard 
@login_required
def clients_view(request):
    
    # Page-level filters
    base_queryset = Client.objects.exclude(client_subgroup='HCP Brokerage').filter(
        client_group='HCP', active_flag='Active')
    
    # Create paginated table
    paginator = Paginator(base_queryset.order_by('-service_start_date'), 10) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

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

    area_data = [
        list(row) for row in base_queryset
        .values_list("area")
        .annotate(count=Count("client_id"))
        .values_list("area", "count")
    ]

    return render(request, "clients/clients_active.html", {
            "page_obj": page_obj,
            "client_group_data": client_group_data,
            "hcp_level_data": hcp_level_data,
            "area_data": area_data
            })


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

