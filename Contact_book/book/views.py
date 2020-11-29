from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views import generic
from .models import ContactBook
from .forms import ContactForm
# Create your views here.

# Original index view before adding the code for a list view
def index(request):
    
    return render(request, 'book/index.html', )

# Shows data taken in a list view
class ContactListView(generic.ListView):
    # Associates the ContactBook Model with this view so django knows what to display
    model = ContactBook
    # Django requires a different naming convention of its templates when using 
    # class based views. So in order to completely override it use the template name
    # attribute and have it equal the directory/app name and template name
    template_name = 'book/index.html'

# View that shows the contact alone 
class ContactDetailView(generic.DetailView):
    model = ContactBook
    template_name = 'book/contact_detail.html'

# Creates the form that will take the users data for the contact.
def book_form(request):
    # checks to make sure that the form created has a POST method attached to it
    if request.method=="POST":
        # If it does the form variable will contain the imported ContactForm 
        # with request.POST as its argument
        form = ContactForm(request.POST)
        # Checks to see if the form is valid 
        if form.is_valid():
            # saves the form to the database
            form.save()
            messages.success(request,f'Contact has been succesfully saved.')
            # redirects the user back to the book form page so they can add more if wanted
            return redirect('book-book_form')
    # If the form doesnt have the post method it will return a blank contactform 
    else:
        form = ContactForm()
    return render(request, 'book/book_form.html',{'form':form})

# creates the view for the about page 
def about(request):
    return render(request, 'book/about.html',)