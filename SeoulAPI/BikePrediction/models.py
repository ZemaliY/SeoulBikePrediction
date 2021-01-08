from django.db import models

# Create your models here.
class locations(models.Model):
    SEASON_CHOICES = (
		('Autumn', 'Autumn'),
		('Spring', 'Spring'),
		('Summer', 'Summer'),
		('Winter', 'Winter'),
	)
    Date=models.CharField(max_length=15) 
    RentedBike=models.FloatField(null=True)
    Hour=models.IntegerField(default=0)
    Temperature=models.FloatField(default=0.0)
    Humidity=models.IntegerField(default=0)
    Wind=models.FloatField(default=0.0)
    Visibility=models.IntegerField(default=0)
    DewPointTemperature=models.FloatField(default=0.0)
    SolarRadiation=models.FloatField(default=0.0)
    Rainfall=models.FloatField(default=0.0)
    Snowfall=models.FloatField(default=0.0)
    Season=models.CharField(max_length=15,choices=SEASON_CHOICES)
    Holiday=models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']



