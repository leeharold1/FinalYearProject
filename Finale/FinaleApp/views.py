from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'FinaleApp/home.html')

def user(request):
    return render(request, 'FinaleApp/user.html')

def business(request):
    return render(request, 'FinaleApp/business.html')

def delivery(request):
    return render(request, 'FinaleApp/delivery.html')

def orders(request):
    return render(request, 'FinaleApp/orders.html')

def bookings(request):
    return render(request, 'FinaleApp/bookings.html')

