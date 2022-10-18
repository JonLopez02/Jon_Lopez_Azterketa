from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Kotxe
# Create your views here.

def index(request):
  kotxeak = Kotxe.objects.all().values()
  template = loader.get_template('kotxeak.html')
  context = {
    'kotxeak': kotxeak,
  }
  return HttpResponse(template.render(context, request))

def addKotxe(request):
  template = loader.get_template('addKotxea.html')
  return HttpResponse(template.render({}, request))

def add(request):
  a = request.POST['izena']
  b = request.POST['alokatze_data']
  x = request.POST['kolorea']
  y = request.POST['modeloa']
  z = request.POST['prezioa']
  kotxe = Kotxe(izena=a, alokatze_data=b, kolorea=x, modeloa=y, prezioa=z)
  kotxe.save()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  kotxe = Kotxe.objects.get(id=id)
  template = loader.get_template('updateKotxe.html')
  context = {
    'kotxe': kotxe,
  }
  return HttpResponse(template.render(context, request))

def updateKotxe(request, id):
  izena = request.POST['izena']
  alokatze_data = request.POST['alokatze_data']
  kolorea = request.POST['kolorea']
  modeloa = request.POST['modeloa']
  prezioa = request.POST['prezioa']
  kotxe = Kotxe.objects.get(id=id)
  kotxe.izena = izena
  kotxe.alokatze_data = alokatze_data
  kotxe.kolorea = kolorea
  kotxe.modeloa = modeloa
  kotxe.prezioa = prezioa
  kotxe.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  kotxe = Kotxe.objects.get(id=id)
  kotxe.delete()
  return HttpResponseRedirect(reverse('index'))
