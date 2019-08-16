from django.conf import settings
from django.db import models
from django.urls import reverse

from djmoney.models.fields import MoneyField


def user_directory_path(instance, file):
    # images will be saved to user seperated folders
    # EXAMPLE: MEDIA_ROOT/properties/owner_1/unit.png
    return 'properties/owner_{}/{}'.format(instance.owner.id, file)


class AbstractPropertyBase(models.Model):
    '''An abastract base model class for both the house and apartment unit model'''
    UNFURNISHED = 'Unfurnished'
    SEMI_FURNISHED = 'Semi furnished'
    FULL_FURNISHED = 'Fully furnished'
    FURNISHING = (
        (UNFURNISHED, 'Unfurnished'),
        (SEMI_FURNISHED,'Semi Furnished'),
        (FULL_FURNISHED, 'Fully Furnished')
    )
    ONE_ROOM = '1 BR'
    TWO_ROOM = '2 BR'
    THREE_ROOM = '3 BR'
    MORE = 'More than 3 BR'
    ROOMS = (
        (ONE_ROOM, '1 Bedroom'),
        (TWO_ROOM, '2 Bedroom'),
        (THREE_ROOM, '3 Bedroom'),
        (MORE, 'More than 3 Bedrooms')
    )

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=55)
    slug = models.SlugField()
    description = models.TextField()
    deposit = MoneyField(max_digits=14, decimal_places=2, default_currency='IDR')
    rent_per_month = MoneyField(max_digits=14, decimal_places=2, default_currency='IDR')
    rent_per_year = MoneyField(max_digits=14, decimal_places=2, default_currency='IDR')

    furnishing = models.CharField(max_length=25, choices=FURNISHING, default=UNFURNISHED)
    bedrooms = models.CharField(max_length=25, choices=ROOMS, default=ONE_ROOM)
    bathroom = models.BooleanField(default=True)
    size = models.PositiveIntegerField(blank=True)
    water_heating = models.BooleanField(default=False)

    available = models.BooleanField(default=True)

    image = models.ImageField(upload_to=user_directory_path, default='properties/default.png')

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-timestamp']

    def __str__(self):
        return self.title 

    def save(self, *args, **kwargs):
        # Override save method to auto calculate total price for
        # property per year
        self.rent_per_year = self.rent_per_month * 12
        super().save(*args, **kwargs)

class House(AbstractPropertyBase):
    ONE = '1'
    TWO = '2'
    THREE = '3'
    MORE = 'More than 3'
    BATHROOMS = (
        (ONE, '1'),
        (TWO, '2'),
        (THREE, '3'),
        (MORE, 'More than 3'),
    )
    garden = models.BooleanField(default=False)
    garage = models.BooleanField(default=False)
    floors = models.PositiveIntegerField()
    bathrooms = models.CharField(max_length=5, choices=BATHROOMS, default=ONE)

    def get_absolute_url(self):
        return reverse('properties:house_detail', kwargs={"slug": self.slug})


class Apartment(models.Model):

    '''Class representing an Apartment'''
    name = models.CharField(max_length=125, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=255)
    # location = .....
    floors = models.IntegerField()
    shopping_mall = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)
    swimming_pool = models.BooleanField(default=False)
    jogging_track = models.BooleanField(default=False)
    laundry = models.BooleanField(default=False)
    security = models.BooleanField(default=False)
    image = models.ImageField(upload_to='properties/apartments', default='properties/default.jpg')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('properties:apartment_detail', kwargs={'slug': self.slug})


class ApartmentUnit(AbstractPropertyBase):
    apartment = models.ForeignKey(Apartment, related_name='units', on_delete=models.CASCADE)
    floor = models.IntegerField(default=3)
    balcony = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('properties:unit_detail', kwargs={'slug': self.slug})
    

    


    
    


    