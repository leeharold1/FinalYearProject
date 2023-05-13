from django.shortcuts import render, redirect
from django.db import connection
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import CreateUserForm, ReserveTableForm, DeliveryForm, CollectionForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Reservations, DeliveryOrder
import json
from django.http import JsonResponse

def home(request):
	return render(request, 'home.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username and/or password is incorrect.")
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
	logout(request)
	return redirect('login')

def create_user(request):
	if request.method == "POST":
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(request, username=username, password=password)
			login(request, user)
			return redirect('home')
	else: 
		form = CreateUserForm()

	return render(request, 'authenticate/create_user.html', {'form':form,},)
	
class UserEditView(generic.CreateView):
	form_class = UserChangeForm
	template_name = 'authenticate/edit_profile.html'
	success_url = reverse_lazy('home')


def delivery(request):
	return render(request, 'BCD/delivery.html', {})

class DeliveryAdd(generic.CreateView):
    form_class = DeliveryForm
    template_name = "BCD/deliveryAdd.html"
    success_url = reverse_lazy('home')

def collection(request):
	return render(request, 'BCD/collection.html', {})

class collectionAdd(generic.CreateView):
    form_class = CollectionForm
    template_name = "BCD/collectionAdd.html"
    success_url = reverse_lazy('home')

def booking(request):
	return render(request, 'BCD/booking.html', {})

class ReserveTable(generic.CreateView):
    form_class = ReserveTableForm
    template_name = "BCD/bookingAdd.html"
    success_url = reverse_lazy('home')