from django.urls import path
from . import views

urlpatterns = [
    path('', 
    views.ContactListView.as_view(), 
    name='book-index'
    ),

    path('contact/<int:pk>', 
        views.ContactDetailView.as_view(), 
        name='contact_detail'
    ),

    path('contact/<int:pk>/update', 
        views.ContactUpdateView.as_view(), 
        name='contact_form'
    ),
    
    path('contact/<int:pk>/delete', 
        views.ContactDeleteView.as_view(), 
        name='contact_delete'
    ),

    path('book_form/', 
        views.book_form, 
        name='book-book_form'
    ),
    
    path('about/', 
        views.about, 
        name='about' 
        )
]