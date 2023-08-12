from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Gear, Retailer

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

class RetailerList(ListView):
    model = Retailer

class RetailerCreate(CreateView):
    model = Retailer
    fields = ['name']

class RetailerDetail(DetailView):
    model = Retailer

class RetailerDelete(DeleteView):
    model = Retailer