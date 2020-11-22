from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method== 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 
                f'You have succesfully created an account! Now you can log in.'
                )
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form})

# decorator that only allows the view to be seen if the user is logged in
@login_required
def profile(request):
    # checks to see if the method on the form is POST
    if request.method == 'POST':
        # if the method if POST load the forms wanted into the template, with the 
        # instance of the user
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, 
            request.FILES, 
            instance=request.user.profile
        )
        # Now check and see if the forms are valid and then saves
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # sends message with success and redirects to the profile route
            messages.success(request, 'Your account info has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)