import sys
import os
import uuid
import random
from django.db.models import Q
from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField
from django.urls import reverse
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.utils.translation import ugettext_lazy as _
from .utils import unique_slug_generator
from PIL import Image
from io import BytesIO
# from django.contrib.auth.models import AbstractUser, BaseUserManager
from .choices import (category_choices,bedroom_choices,bathroom_choices)
from django.core.files.uploadedfile import InMemoryUploadedFile

 

# Create a dynamic file path for house images by user
def get_upload_path(instance, filename):
    return os.path.join(
      "users", "sale", "user_%d" % instance.seller.id, "house_%s" % instance.slug, filename
      )
def get_upload_path_rental(instance, filename):
    return os.path.join(
      "users", "rent", "user_%d" % instance.seller.id, "house_%s" % instance.slug, filename
      )


# Define City model
class City(models.Model):
    title        = models.CharField(max_length=120, blank=True, unique=True)
    slug         = models.SlugField(blank=True, unique=True)
    
    def get_city_url(self):
        return reverse("post-city", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
    
    def get_post(self):
        return post.objects.filter(city__title = self.title)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'



# Define Neighborhood model
class Neighborhood(models.Model):
    title        = models.CharField(max_length=120, blank=True, unique=True)
    slug         = models.SlugField(null=True, blank=True, unique=True)
    city         = models.ForeignKey(City,blank=True, default="", max_length=300, unique=False, on_delete=models.CASCADE)
    
    def get_neighborhood_url(self):
        return reverse("post-neighborhood", kwargs={"slug": self.city.slug, "neighborhood_slug": self.slug})


    def __str__(self):
        return self.title
    
    
    def get_post(self):
        return post.objects.filter(neighborhood__title = self.title)

    class Meta:
        verbose_name = 'Neighborhood'
        verbose_name_plural = 'Neighborhoods'




# Define Custom Queryset
class PostQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active__contains=1, admin_approved__contains=1)

    def featured(self):
        return self.filter(featured__contains=1, active__contains=1)

    def search(self, query):
        lookups = (Q(city__title__icontains=query) |
                   Q(neighborhood__title__icontains=query) 
                   )
        return self.filter(lookups).distinct()


# Define Custom Manager
class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()#.active()

    def featured(self):
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)


# Define Post model
class Post(models.Model):
    # id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=32)
    seller = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)
    # title = models.CharField(default="", max_length=120, blank=True)
    slug = models.SlugField(default="", unique=True, max_length=500)
    category = models.ForeignKey(Category, default=2, max_length=30, unique=False, on_delete=models.CASCADE, related_name='postscategory')
    city = models.ForeignKey(City, default="", max_length=30, unique=False, on_delete=models.CASCADE, related_name='postscity')
    neighborhood = models.ForeignKey(Neighborhood, default="", max_length=50, unique=False, on_delete=models.CASCADE, null=True, related_name='postsneighborhood')
    # state = models.CharField(default="", max_length=100)
    zipcode = models.IntegerField(default=0, blank=True, null=True) 
    address = models.CharField(default="", max_length=500)
    sqft = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    facing = models.CharField(max_length=10, default="", unique=False)
    # floor = models.CharField(max_length=10, default="", unique=False)
    house_type = models.CharField(max_length=30, default="", unique=False, verbose_name="House Type")
    beds = models.CharField(max_length=10, choices=bedroom_choices, unique=False)
    baths = models.CharField(max_length=10, choices=bathroom_choices, unique=False)
    new_construction = models.BooleanField(default=False, blank=True, verbose_name="New Construction")
    ready_to_move = models.BooleanField(default=False, blank=True, verbose_name="Ready To Move")
    furnished = models.BooleanField(default=False, blank=True)
  
