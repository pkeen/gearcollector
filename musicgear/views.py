from django.shortcuts import render

# Create your views here.

gear = [
    {'make': 'The Loar', 'model': 'LH-204 Brownstone', 'category': 'guitar'}
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def my_gear_index(request):
    return render(request, 'mygear.html', {
        'gear': gear
    })

