from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='book-index'),
    path('book_form/', views.book_form, name='book-book_form')
    
]