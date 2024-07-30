from django.shortcuts import render, redirect
from .forms import GameForm
from .models import Game

# Create your views here.

# Home page
def homeView(request):
    return render(request, 'gameboxdApp/home.html')

# Page to create Game entry
def createGameView(request):
    form = GameForm()#
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gameList')
    return render(request, 'gameboxdApp/gameForm.html', {'form':form})

# Page to read Game entry
def readGameView(request):
    games = Game.objects.all()
    return render(request, 'gameboxdApp/gameList.html', {'games':games})

# Page to update the Game entry
def updateGameView(request, gameID):
    game = Game.objects.get(gameID=gameID)
    form = GameForm(instance=game)
    if request.method == "POST":
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('gameList')
    return render(request, 'gameboxdApp/gameForm.html', {'form':form})

# Page to delete the Game entry
def deleteGameView(request, gameID):
    game = Game.objects.get(gameID=gameID)
    if request.method == "POST":
        game.delete()
        return redirect('gameList')
    return render(request, 'gameboxdApp/gameConfirmDelete.html', {'game':game})