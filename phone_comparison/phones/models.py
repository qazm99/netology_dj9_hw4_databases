from django.db import models

# Create your models here.

class Phone(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(null=True, blank=True)
    image = models.CharField(null=True, blank=True, max_length=255)
    core_num = models.IntegerField(null=True, blank=True)
    core_frequency = models.FloatField(null=True, blank=True)
    ram_volume = models.IntegerField(null=True, blank=True)
    rom_volume = models.IntegerField(null=True, blank=True)
    lte_exists = models.BooleanField(null=True, blank=True)
    wifi_version = models.CharField(null=True, blank=True, max_length=255)
    bluetooth_version = models.CharField(null=True, blank=True, max_length=255)
    nfc_exists = models.BooleanField(null=True, blank=True)

    #release_date = models.DateField()
    #slug = models.CharField(max_length=255)
    def __str__(self):
        return self.name