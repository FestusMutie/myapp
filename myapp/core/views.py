from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here
def landing_page(request):
    return render(request, 'core/landing.html')

@login_required
def home_page(request):
    return render(request, 'core/home.html')

@login_required
def user_page(request):
    return render(request, 'core/user.html')

@login_required
def album_page(request):
    return render(request, 'core/album.html')

@login_required
def photo_page(request):
    return render(request, 'core/photo.html')

@login_required
def login_page(request):
    return render(request, 'core/login.html')



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
