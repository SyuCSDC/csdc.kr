from django.urls import path
from . import views

app_name='board'

urlpatterns = [
    path('notice/', views.noticeBoard_list, name='noticeBoard_list'),
    path('notice/<int:board_id>/', views.noticeBoard_detail, name='noticeBoard_detail'),
    path('notice/board_create/', views.noticeBoard_create, name='noticeBoard_create'),
    path('notice/<int:board_id>/update/', views.noticeBoard_update, name='noticeBoard_update'),
    path('notice/<int:board_id>/delete/', views.noticeBoard_delete, name='noticeBoard_delete'),
    path('free/', views.freeBoard_list, name='freeBoard_list'),
    path('free/<int:board_id>/', views.freeBoard_detail, name='freeBoard_detail'),
    path('free/board_create/', views.freeBoard_create, name='freeBoard_create'),
    path('free/<int:board_id>/update/', views.freeBoard_update, name='freeBoard_update'),
    path('free/<int:board_id>/delete/', views.freeBoard_delete, name='freeBoard_delete'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    # path('<int:board_id>/comment/', views.comment_create, name='comments_create'),
    # path('<int:board_id>/comment/<int:comment_id>/delete/', views.comment_delete, name='comments_delete'),
]