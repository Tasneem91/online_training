from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.address})'


class Participant(models.Model):
    email = models.EmailField(unique=True)

class Course(models.Model):
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True)
    teacher = models.TextField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    hours = models.TextField(max_length=20)
    participant = models.ManyToManyField(Participant, blank=True, null=True)


    def __str__(self):
        return f'{self.title} - {self.slug}'
