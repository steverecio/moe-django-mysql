from django.db import models

class Moe(models.Model):
    url = models.CharField(max_length=200)

