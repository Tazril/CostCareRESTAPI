from django.db import models

# Create your models here.


class Hospital(models.Model):
    name = models.CharField(max_length=50)
    web_url = models.URLField(max_length=200)
    query_url = models.URLField(max_length=200)
    contact_num = models.BigIntegerField()
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return self.name


class Procedure(models.Model):
    name = models.CharField(max_length=50, unique=True)
    charge = models.FloatField()
    hospital = models.ForeignKey(
        Hospital, on_delete=models.CASCADE, related_name='procedures')
    last_updated = models.DateField(
        auto_now_add=True, verbose_name='last updated')

    def __str__(self):
        return self.name
