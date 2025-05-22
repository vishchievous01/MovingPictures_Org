from django.db import models


class RegisterDB(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=150, null=True, blank=True)
    Password = models.CharField(max_length=150, null=True, blank=True)



