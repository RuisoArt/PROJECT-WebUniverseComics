from django.db import models


# Create your models here.

class Universe(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    date_foundation = models.DateField()
    image_universe = models.CharField(max_length=220)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'universe'


class Characters(models.Model):
    universe = models.ForeignKey(Universe, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=3000)
    imagen = models.CharField(max_length=220)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'characters'


class Powers(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'powers'


class powers_character(models.Model):
    powers = models.ForeignKey(Powers, on_delete=models.CASCADE)
    characters = models.ForeignKey(Characters, on_delete=models.CASCADE)
    number = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'powers_characters'
