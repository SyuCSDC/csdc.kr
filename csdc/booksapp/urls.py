from django.urls import path
from .views import ProfileListView , ProfileDetailView , BookListView , BookDetailView

urlpatterns = [
    path('profiles/', ProfileListView.as_view(), name='profile_list'),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('bookslist/', BookListView.as_view(), name='book_list'),
    path('bookslist/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
]