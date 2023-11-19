from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('changeSimulationState', views.changeSimulationState, name='changeSimulationState'),
    path('getUpdatedData', views.getUpdatedData, name='getUpdatedData'),
]