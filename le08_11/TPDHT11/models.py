import os

from django.contrib.auth.models import User
from django.core.mail import send_mail

from django.db import models

# Create your models here.
from twilio.rest import Client


class Dht(models.Model):
    temp = models.FloatField(null=True)
    hum = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.temp)
"""
    def save(self, *args, **kwargs):
        if self.temp > 40:
            from TPDHT11.views import sendtele
            sendtele()
            send_mail(
                'température dépasse la normale,' + str(self.temp),
                'anomalie dans la machine le,' + str(self.dt),
                'yassine.ayat@ump.ac.ma',
                ['yassine1960ayat@gmail.com'],
                fail_silently=False,
            )

        return super().save(*args, **kwargs)
    """
