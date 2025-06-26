# pages/urls.py
from django.urls import path
from .views import home_page_view, about_page_view, \
    clients_view, clients_new_view, clients_exited_view, \
    clients_brokerage_view, clients_external_services_view, \
    employee_view, service_view, travel_view, case_manager_view


urlpatterns = [
    path("", home_page_view, name="home"),
    path("about/", about_page_view, name="about"),

    # Clients dashboard
    path("clients/active/", clients_view, name="clients-active"),
    path("clients/new/", clients_new_view, name="clients-new"),
    path("clients/exited/", clients_exited_view, name="clients-exited"),
    path("clients/brokerage/", clients_brokerage_view, name="clients-brokerage"),
    path("clients/external-services/", clients_external_services_view, name="clients-external-services"),

    # Employees dashboard
    path("employees/", employee_view, name="employees"),

    # Service Hours dashboard
    path("services/", service_view, name="services"),

    # Travel dashboard
    path("travel/", travel_view, name="travel"),

    # Case Manager
    path("case-manager/", case_manager_view, name="case-manager"),
]

