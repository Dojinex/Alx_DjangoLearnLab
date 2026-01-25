from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from .views import register
from .views import admin_view
from .views import can_add_book
from .views import can_delete_book
from .views import can_change_book
from . import librarian_view
from . import member_view
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('books/', list_books, name='all_books'),
    path('library/<int:pk>', LibraryDetailView.as_view(), name='library'),
    path('register', register, name='register'),
    path('login', LoginView.as_view(template_name='relationship_app/logint.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admins', admin_view, name='admins'),
    path('librarians', librarian_view.librarian_view, name='librarians'),
    path('members', member_view.member_view, name='members'),
    path('add_book/', can_add_book),
    path('edit_book/', can_change_book),
    path('delete_book/', can_delete_book),
]