from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Gear

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def gear_index(request):
    gear = Gear.objects.all()
    return render(request, 'mygear.html', {
        'gear': gear
    })

def gear_detail(request, gear_id):
    gear = Gear.objects.get(id=gear_id)
    return render(request, 'musicgear/detail.html', {
        'gear': gear
    })

class GearCreateView(CreateView):
    model = Gear
    fields = '__all__'

class GearUpdate(UpdateView):
    model = Gear
    fields = '__all__'

class GearDelete(DeleteView):
    model = Gear