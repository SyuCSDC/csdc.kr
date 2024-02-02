from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Profile,Book

# Create your views here.
class ProfileListView(ListView):
    model = Profile
    context_object_name = 'profiles'
    template_name = 'profiles/profile_list.html'

class ProfileDetailView(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profiles/profile_detail.html'

class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/book_list.html'

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'



    