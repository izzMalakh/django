from django.db import models


class Dojo(models.Model):
    name = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=255,null=True)
    state = models.CharField(max_length=2,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #Ninjas =

class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="Ninjas", on_delete = models.CASCADE)
    first_name = models.CharField(max_length=255,null=True)
    last_name = models.CharField(max_length=255,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
