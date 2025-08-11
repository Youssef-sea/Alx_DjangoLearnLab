# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Profile View
@login_required
def profile(request):
    if request.method == 'POST':
        # Handle profile updates, e.g., changing email
        new_email = request.POST.get('email')
        if new_email:
            request.user.email = new_email
            request.user.save()
            # Add a message to the user confirming the update
            return redirect('profile')
    return render(request, 'registration/profile.html', {'user': request.user})