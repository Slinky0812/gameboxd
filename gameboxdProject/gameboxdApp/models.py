from django.db import models

# Create your models here
class Game(models.Model):
    gameID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    devStudio = models.CharField(max_length=128)
    price = models.FloatField()
    avgRating = models.FloatField()
    numOfReviews = models.IntegerField()
    
    def __str__(self):
        return self.name