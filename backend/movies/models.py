from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    actors = models.ManyToManyField(
        Actor,
        related_name="movies",
        blank=True,
    )

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
    
class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        related_name="reviews",
        on_delete=models.CASCADE,
    )
    grade = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ],
    )

    def __str__(self):
        return f"{self.movie.title} - {self.grade}/5"