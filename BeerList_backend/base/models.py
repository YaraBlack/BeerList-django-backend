from django.db import models, transaction
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Beer(models.Model):
    """
    This class represent a Beer object.

    Attributes:
        name (str): The name of the beer. Max length is 255 chars.
        brewery (Brewery): The brewery object. Connects the brewery and the beer.
        alcohol (decimal): The alcohol percentage for the beer. Max length is 3 digits.
        ingredients (str): Describes the ingredients for the beer. Max length is 255 chars.
        style (str): Represents the style of the beer. Max length is 80 chars.
        description (str): Represents the description for the beer. Max length is 255 chars.
        image (ImageField): Represents the path for the image to the corresponding beer entry.
        created (DateTimeField): Represents the date and time of an entry's creation.
        updated (DateTimeField): Represents the date and time of an entry's update
    """

    name = models.CharField(max_length=255)
    alcohol = models.DecimalField(max_digits=3, decimal_places=1)
    ingredients = models.CharField(max_length=255)
    style = models.CharField(max_length=80)
    description = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # image = models.ImageField(upload_to='images/beer/') # requires Pillow

    class Meta:
        ordering = ["name"]


class Brewery(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    country = models.CharField(max_length=90, null=True, blank=True)
    city = models.CharField(max_length=189, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    founding_year = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(9999)],
        null=False,
        blank=False,
    )
    rating = models.DecimalField(
        max_digits=2, decimal_places=1, default=0.00, null=False, blank=False
    )
    # logo = models.ImageField(upload_to="images/brewery/") # requires Pillow
    website = models.URLField(max_length=255, null=True, blank=True)
    instagram_url = models.URLField(max_length=255, null=True, blank=True)
    facebook_url = models.URLField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ["name"]


class BeerBrewery(models.Model):
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    # contribution_percentage = models.DecimalField(max_digits=5,
    #   decimal_places=2, null=True, blank=True)
