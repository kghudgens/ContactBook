from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages
# Create your views here.

def index(request):
    
    return render(request, 'book/index.html', )

def book_form(request):
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Contact has been succesfully saved.')
    else:
        form = ContactForm()
    return render(request, 'book/book_form.html',{'form':form})