from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("reports", views.ReportListView.as_view(), name="report_list"),
    path("authorized", views.AuthorizedView.as_view()),
    path("login", views.LoginInterfaceView.as_view(), name="login"),
    path("loggedout", views.LogoutInterfaceView.as_view(), name="loggedout"),
    path("signup", views.SignupView.as_view(), name="signup"),
    path("report/new", views.ReportCreateView.as_view(), name="create_report"),
    path("report/<int:pk>", views.ReportDetailView.as_view(), name="report_detail"),
    path("report/<int:pk>/edit", views.ReportUpdateView.as_view(), name="report_update"),
    path("report/<int:pk>/delete", views.ReportDeleteView.as_view(), name="report_delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)