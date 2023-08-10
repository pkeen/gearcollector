from django.urls import path
from . import views
from .views import GearCreateView, GearUpdate, GearDelete

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('mygear/', views.gear_index, name='index'),
    path('gear/<int:gear_id>', views.gear_detail, name='detail'),
    path('gear/create', GearCreateView.as_view(), name='gear_create'),
    path('gear/<int:pk>/update', GearUpdate.as_view(), name='gear_update'), 
    path('gear/<int:pk>/delete', GearDelete.as_view(), name='gear_delete'), 
]


