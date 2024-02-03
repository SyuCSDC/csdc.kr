from django.urls import path
from .views import list_mentorships, create_mentorship_request, mentorship_detail

urlpatterns = [
    path('mentorships/', list_mentorships, name='list_mentorships'),
    path('mentorships/create/', create_mentorship_request, name='create_mentorship_request'),
    path('mentorships/<int:id>/', mentorship_detail, name='mentorship_detail'),
    
]
