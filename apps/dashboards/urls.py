from django.urls import path
from .views import DashboardsView



urlpatterns = [
    path(
        "auth/dashboards/",
        DashboardsView.as_view(template_name="dashboard_analytics.html"),
        name="index",
    )
]
