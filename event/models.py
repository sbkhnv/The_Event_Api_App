from django.db import models

# Create your models here.
class Speakers(models.Model):
    image = models.ImageField(upload_to="speakers/speakers")
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    Speciality = models.CharField(max_length=20)
    create_date = models.DateField(auto_created=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Speakers'
        verbose_name_plural = 'Speakers'
        ordering = ['first_name']
        indexes = [
            models.Index(fields=['first_name'])
        ]

class Schedule(models.Model):
    image = models.ImageField(upload_to="speakers/speakers")
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    theme = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedule'
        ordering = ['first_name']
        indexes = [
            models.Index(fields=['first_name'])
        ]

class Hotels(models.Model):
    image = models.ImageField(upload_to="hotels/hotels")
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Hotels'
        verbose_name_plural = 'Hotels'
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]

class Gallery(models.Model):
    images = models.ImageField(upload_to="gallery/gallery")

class Sponsors(models.Model):
    images = models.ImageField(upload_to="sponsors/sponsors")

class Tickets(models.Model):
    type = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    count = models.PositiveBigIntegerField(default=0)
    description_1 = models.CharField(max_length=20)
    description_2 = models.CharField(max_length=20)
    description_3 = models.CharField(max_length=20)
    description_4 = models.CharField(max_length=20)
    description_5 = models.CharField(max_length=20)
    description_6 = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.type} {self.price}'

    class Meta:
        verbose_name = 'Tickets'
        verbose_name_plural = 'Tickets'
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]