from django.shortcuts import render
from django.http import HttpResponse


def index(request, card_id):
  return render(request, 'cards/index.html', {'card': card_id})

# Create your views here.
