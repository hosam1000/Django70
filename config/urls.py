from django.contrib import admin
from django.urls import include, path
from web_project.views import SystemView
from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls),

    # Redirect root URL to login
    path("", lambda request: redirect('auth-login-basic'), name='root_redirect'),

    # Dashboard urls
    path("", include("apps.dashboards.urls")),

    # Layouts urls
    path("", include("apps.layouts.urls")),

    # Pages urls
    path("", include("apps.pages.urls")),

    # Card urls
    path("", include("apps.cards.urls")),

    # UI urls
    path("", include("apps.ui.urls")),

    # Extended UI urls
    path("", include("apps.extended_ui.urls")),

    # Icons urls
    path("", include("apps.icons.urls")),

    # Forms urls
    path("", include("apps.forms.urls")),

    # FormLayouts urls
    path("", include("apps.form_layouts.urls")),

    # Tables urls
    path("", include("apps.tables.urls")),
]

handler404 = SystemView.as_view(template_name="pages_misc_error.html", status=404)
handler400 = SystemView.as_view(template_name="pages_misc_error.html", status=400)
handler500 = SystemView.as_view(template_name="pages_misc_error.html", status=500)
