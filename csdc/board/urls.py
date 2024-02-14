from django.urls import path
from . import views

app_name='board'

urlpatterns = [
    path('board_list/', views.board_list, name='board_list'),
    path('<int:board_id>/', views.board_detail, name='board_detail' ),
    path('board_create/', views.board_create, name='board_create'),
    path('<int:board_id>/update/', views.board_update, name='board_update'),
    path('<int:board_id>/delete/', views.board_delete, name='board_delete'),
]