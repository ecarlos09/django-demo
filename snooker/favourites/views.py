from django.shortcuts import render
from django.http import HttpResponse

from .models import Player

# Create your views here. (These are more like controllers)

players_list = [
    {"id": 1, "name": 'Mark Selby', "nationality": 'English'},
    {"id": 2, "name": 'Judd Trump', "nationality": 'English'}
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def players(request):
    data = { 'snooker_players': Player.objects.all() }
    return render(request, 'players.html', data)

def show(request, id):
    player = get_object_or_404(Dog, pk=id)
    data = { 'player': player }
    return render(request, 'show.html', data)

def not_found_404(request, exception):
    data = {"err": exception }
    return render(request, '404.html', data)

def server_error_500(request):
    return render(request, '500.html')