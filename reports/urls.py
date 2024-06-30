from django.urls import path
from .views import ReportListView, ReportDetailView, ReportCreateView, ReportUpdateView, ReportLikeView, ReportDeleteView

app_name = "reports"
urlpatterns = [
    path('', ReportListView.as_view(), name="report-list"),
    path("<int:pk>/", ReportDetailView.as_view(), name="report-detail"),
    path("<int:pk>/edit/", ReportUpdateView.as_view(), name="report-update"),
    path("<int:pk>/like/", ReportLikeView.as_view(), name="report-like"),
    path("<int:pk>/delete/", ReportDeleteView.as_view(), name="report-delete"),
    path("create/", ReportCreateView.as_view(), name="report-create"),
]