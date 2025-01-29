from django.db import models

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
