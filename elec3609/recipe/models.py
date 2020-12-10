from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
import sys
from PIL import Image
from io import BytesIO
from django.core.files import File


# Post - With help from:
# https://tutorial.djangogirls.org/en/django_models/

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=75, null=True, blank=False)
    content = models.TextField()
    picture = models.ImageField(upload_to='post_images', null=True, blank=True)
    timestamp = models.DateField(auto_now_add=True)

    category_choices = [
        ('AussieBBQ', 'AussieBBQ'),
        ('BakedSweets', 'BakedSweets'),
        ('Bread', 'Bread'),
        ('Breakfast', 'Breakfast'),
        ('Burgers', 'Burgers'),
        ('Chinese', 'Chinese'),
        ('Dessert', 'Dessert'),
        ('Drinks', 'Drinks'),
        ('Fried Food', 'Fried Food'),
        ('Greek', 'Greek'),
        ('Indian', 'Indian'),
        ('Japanese', 'Japanese'),
        ('Lebanese', 'Lebanese'),
        ('Mexican', 'Mexican'),
        ('Pasta', 'Pasta'),
        ('Pastries', 'Pastries'),
        ('Pies', 'Pies'),
        ('Pizza', 'Pizza'),
        ('Rice', 'Rice'),
        ('Salad', 'Salad'),
        ('Sandwich', 'Sandwich'),
        ('Seafood', 'Seafood'),
        ('Snacks', 'Snacks'),
        ('Soup', 'Soup'),
        ('Steak', 'Steak'),
        ('Thai', 'Thai'),
        ('Vegetarian', 'Vegetarian'),
    ]

    category = models.CharField(
        max_length = 20,
        choices = category_choices,
    )

    # truncated post content for previews
    @property
    def short_content(self):
        if len(self.content) < 200:
            return self.content
        else:
            return self.content [:200] + '...'
            
    @property
    def post_img(self):
        if self.picture and hasattr(self.picture, 'url'):
            return self.picture.url

# User = setting.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    firstname = models.CharField(max_length=75, null=True, blank=True)
    lastname = models.CharField(max_length=75, null=True, blank=True)
    bio = models.TextField(max_length=200, null=True, blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    favorites = models.ManyToManyField(Post)