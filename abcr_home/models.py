from django.db import models

# Create your models here.

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_rating = models.DecimalField(max_digits=2, decimal_places=1,default=0)
    hotel_review_count = models.IntegerField(default=0)
    trip_link = models.CharField(max_length=1000)

    def __str__(self):
        return self.hotel_name

class Summary(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    aspect = models.CharField(max_length=50)
    text = models.CharField(max_length=600)
    sentiment = models.CharField(max_length=25)
    user = models.CharField(max_length=200)
    sentiment_score = models.FloatField(default=0)
    ranking_score = models.FloatField(default=0)

    def __str__(self):
        return self.text