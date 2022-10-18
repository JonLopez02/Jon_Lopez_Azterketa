from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addPertsona/', views.addPertsona, name='addPertsona'),
    path('addPertsona/add/', views.add, name='add'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updatePertsona/<int:id>', views.updatePertsona, name='updatePertsona'),
]