from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

class Flight(models.Model):
    flightnumber                = models.CharField(max_length=10)
    operatingAirlines           = models.CharField(max_length=20)
    departureCity               = models.CharField(max_length=20)
    arrivalCity                 = models.CharField(max_length=20)
    dateOfDeparture             = models.DateField()
    estimatedTimeOfDeparture    = models.TimeField()

class Passenger(models.Model):
    firstname = models.CharField(max_length=20)
    lastname  = models.CharField(max_length=20)
    middlename= models.CharField(max_length=20,blank=True,null=True)
    email     = models.CharField(max_length=20)
    phone     = models.CharField(max_length=13)

class Reservation(models.Model):
    flight       = models.ForeignKey(Flight,on_delete=models.CASCADE) 
    passenger    = models.ForeignKey(Passenger,on_delete=models.CASCADE) 

#Django singnal handeler method receive post_svae singnal the create the token for that user.
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def createAuthToken(sender,instance,created,**kwargs):
    if created:
        Token.objects.create(user=instance)


