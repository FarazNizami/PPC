from django.urls import path
from . import views

urlpatterns = [
    path('blastfurnace', views.blastfurnace, name='blastfurnace'),
    path('', views.home, name='home'),
    path('rmhs', views.home, name='rmhs'),
    path('cpp_pci_weights', views.cpp_pci_weights, name='cpp_pci_weights')
]
