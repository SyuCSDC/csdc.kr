from django.urls import path
from .views import ReportListView, ReportCreateView, ReportDetailView

app_name = "report"

urlpatterns = [
    path('report_list/', ReportListView.as_view(), name='report_list'),
    path('create/', ReportCreateView.as_view(), name='report_create'),
    path('<int:pk>/', ReportDetailView.as_view(), name='report_detail'),
    # 추가적인 URL 패턴이 필요할 경우 여기에 정의
]
