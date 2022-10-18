from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Pertsona


def index(request):
  pertsonak = Pertsona.objects.all().values()
  template = loader.get_template('kotxeak.html')
  context = {
    'pertsonak': pertsonak,
  }
  return HttpResponse(template.render(context, request))

def addPertsona(request):
  template = loader.get_template('addPertsona.html')
  return HttpResponse(template.render({}, request))

def add(request):
  x = request.POST['izena']
  y = request.POST['abizena']
  z = request.POST['herria']
  pertsona = Pertsona(izena=x, abizena=y, herria=z)
  pertsona.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  pertsona = Pertsona.objects.get(id=id)
  pertsona.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  pertsona = Pertsona.objects.get(id=id)
  template = loader.get_template('updatePertsona.html')
  context = {
    'pertsona': pertsona,
  }
  return HttpResponse(template.render(context, request))

def updatePertsona(request, id):
  izena = request.POST['izena']
  abizena = request.POST['abizena']
  herria = request.POST['herria']
  pertsona = Pertsona.objects.get(id=id)
  pertsona.izena = izena
  pertsona.abizena = abizena
  pertsona.herria = herria
  pertsona.save()
  return HttpResponseRedirect(reverse('index'))