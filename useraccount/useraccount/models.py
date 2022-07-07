from django.db import models

class Useraccount(models.Model):
    accountname = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    accountid = models.CharField(max_length=100)
