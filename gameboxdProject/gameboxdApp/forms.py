from django import forms
from .models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
        labels = {
            'gameID': 'Game ID',
            'name': 'Name',
            'devStudio': 'Developer Studio',
            'price': 'Price',
            'avgRating': 'Average Rating',
            'numOfReviews': 'Number of Reviews',   
        }
        widget = {
            'gameID': forms.NumberInput(attrs={'placeholder':'e.g. 1', 'class':'form-control'}),
            'name': forms.TextInput(attrs={'placeholder':'e.g. Elden Ring', 'class':'form-control'}),
            'devStudio': forms.TextInput(attrs={'placeholder':'e.g. FromSoftware', 'class':'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder':'e.g. 19.99', 'class':'form-control'}),
            'avgRating': forms.NumberInput(attrs={'placeholder':'e.g. 1', 'class':'form-control'}),
            'numOfReviews': forms.NumberInput(attrs={'placeholder':'e.g. 1', 'class':'form-control'}),
        }