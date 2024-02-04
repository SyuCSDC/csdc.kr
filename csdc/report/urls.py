from django.urls import path
from .views import ReportListView, ReportCreateView, ReportDetailView , ReportUpdateView , BookcreateView , BookListView

app_name = "report"

urlpatterns = [
    path('report_list/', ReportListView.as_view(), name='report_list'),
    path('create/', ReportCreateView.as_view(), name='report_create'),
    path('<int:pk>/', ReportDetailView.as_view(), name='report_detail'),
    path('<int:pk>/update/' , ReportUpdateView.as_view(), name='report_update'),
    path('book_request/', BookcreateView.as_view(), name='book_request'),
    path('book_list/' , BookListView.as_view(), name='book_list'),
    
    # 추가적인 URL 패턴이 필요할 경우 여기에 정의
]
  