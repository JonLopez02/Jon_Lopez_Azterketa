from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addKotxe/', views.addKotxe, name='addKotxe'),
    path('addKotxe/add/', views.add, name='add'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updateKotxe/<int:id>', views.updateKotxe, name='updateKotxe'),
    path('delete/<int:id>', views.delete, name='delete'),
]
