from django.db import models

# Create your models here.

def Location(models.Model):
    address_line1= models.CharField(max_length=255, hrlp_text="street address, P.O. Box, company name, c/o")
    address_line2 = models.CharField(max_length=255, blank=True, null=True, help_text="Apartment, suite, unit, building, floor, etc.")
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    countary = models.CharField(max_length=100, default="India")

    class Meta:
        verbose_name = "Location"
        verbose_name_prural = "Locations"

    def __str__(self):
        return f"{self.addrss_line1}, {self,city}, {self.state} {self.zip_code}"

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = Location()
    opening_house = models.JSONField(default=dict)

    def __str__(self):
        return self.name