from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Beasiswa, Mahasiswa
from .forms import BeasiswaForm, MahasiswaForm, LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def beasiswa_list(request):
    beasiswa_list = Beasiswa.objects.all()
    return render(request, 'beasiswa_app/admin/beasiswa_list.html', {'beasiswa_list': beasiswa_list})

def apply_beasiswa(request):
    if request.method == 'POST':
        form = BeasiswaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('beasiswa_list')
    else:
        form = BeasiswaForm()
    return render(request, 'beasiswa_app/mahasiswa/apply_beasiswa.html', {'form': form})

def status_beasiswa(request):
    mahasiswa = Mahasiswa.objects.get(pk=request.user.id)
    status_beasiswa = Beasiswa.objects.filter(pemohon=mahasiswa)
    return render(request, 'beasiswa_app/mahasiswa/status_beasiswa.html', {'status_beasiswa': status_beasiswa})

@login_required(login_url='beasiswa_app:login')
def profile(request):
    if request.method == 'POST':
        form = MahasiswaForm(request.POST, instance=request.user.mahasiswa)
        if form.is_valid():
            form.save()
    else:
        form = MahasiswaForm(instance=request.user.mahasiswa)
    return render(request, 'beasiswa_app/mahasiswa/profile.html', {'form': form})


@login_required(login_url='beasiswa_app:login')
def manage_beasiswa(request):
    beasiswa_list = Beasiswa.objects.all()
    return render(request, 'beasiswa_app/admin/beasiswa_list.html', {'beasiswa_list': beasiswa_list})

@login_required(login_url='beasiswa_app:login')
def manage_mahasiswa(request):
    mahasiswa_list = Mahasiswa.objects.all()
    return render(request, 'beasiswa_app/admin/manage_mahasiswa.html', {'mahasiswa_list': mahasiswa_list})

@login_required(login_url='beasiswa_app:login')
def message_list(request):
    messages = Mahasiswa.objects.all()
    return render(request, 'beasiswa_app/admin/message_list.html', {'messages': messages})

def mahasiswa_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('beasiswa_app:login')
    else:
        form = RegisterForm()
    return render(request, 'beasiswa_app/mahasiswa/auth/register.html', {'form': form})

def mahasiswa_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('beasiswa_app:profile')
            else:
                form.add_error(None, "Username or password is incorrect.")
    else:
        form = LoginForm()
    return render(request, 'beasiswa_app/mahasiswa/auth/login.html', {'form': form})

def mahasiswa_logout(request):    
    logout(request)
    return redirect('beasiswa_app:home')

def home(request):
    return render(request, 'home.html')
