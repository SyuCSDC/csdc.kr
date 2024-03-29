from django.urls import path
from . import views

app_name='board'

urlpatterns = [
    path('notice/', views.noticeBoard_list, name='noticeBoard_list'),
    path('notice/<int:board_id>/', views.noticeBoard_detail, name='noticeBoard_detail'),
    path('notice/board_create/', views.noticeBoard_create, name='noticeBoard_create'),
    path('notice/<int:board_id>/update/', views.noticeBoard_update, name='noticeBoard_update'),
    path('notice/<int:board_id>/delete/', views.noticeBoard_delete, name='noticeBoard_delete'),
    path('study/', views.studyBoard_list, name='studyBoard_list'),
    path('study/<int:board_id>/', views.studyBoard_detail, name='studyBoard_detail'),
    path('study/board_create/', views.studyBoard_create, name='studyBoard_create'),
    path('study/<int:board_id>/update/', views.studyBoard_update, name='studyBoard_update'),
    path('study/<int:board_id>/delete/', views.studyBoard_delete, name='studyBoard_delete'),
    path('free/', views.freeBoard_list, name='freeBoard_list'),
    path('free/<int:board_id>/', views.freeBoard_detail, name='freeBoard_detail'),
    path('free/board_create/', views.freeBoard_create, name='freeBoard_create'),
    path('free/<int:board_id>/update/', views.freeBoard_update, name='freeBoard_update'),
    path('free/<int:board_id>/delete/', views.freeBoard_delete, name='freeBoard_delete'),
    path('question/', views.question_list, name='questionBoard_list'),
    path('question/<int:board_id>/', views.questionBoard_detail, name='questionBoard_detail'),
    path('question/board_create/', views.questionBoard_create, name='questionBoard_create'),
    path('question/<int:board_id>/update/', views.questionBoard_update, name='questionBoard_update'),
    path('question/<int:board_id>/delete/', views.questionBoard_delete, name='questionBoard_delete'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    # path('<int:board_id>/comment/', views.comment_create, name='comments_create'),
    # path('<int:board_id>/comment/<int:comment_id>/delete/', views.comment_delete, name='comments_delete'),
]