from django.urls import path
from .views import list_mentorships, create_mentorship_request, edit_mentorship , delete_mentorship

app_name = 'mentorship'

urlpatterns = [
    path('mentorship_list/', list_mentorships, name='list_mentorships'),
    path('create/', create_mentorship_request, name='create_mentorship_request'),
    # path('<int:id>/', mentorship_detail, name='mentorship_detail'),
    path('<int:pk>/', edit_mentorship , name='edit_mentorship'),
    path('<int:pk>/delete/', delete_mentorship , name='delete_mentorship'),
    
]
