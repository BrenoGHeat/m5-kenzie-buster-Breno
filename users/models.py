from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(max_length=127, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField(null=True, default=None)
    is_employee = models.BooleanField(default=False)

    movies_purchased = models.ManyToManyField(
        Movie, through="movies_orders.MovieOrder", related_name="user_buyers"
    )
