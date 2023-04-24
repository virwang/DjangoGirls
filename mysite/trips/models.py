from datetime import datetime
from django.db import models

# Create your models here.
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Trip(models.Model):
    trip_title = models.CharField(max_length=100)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    country = models.CharField(max_length=100)
    airplane = models.CharField(max_length=100)
    group_name = models.CharField(max_length=100)
    amount = models.BigIntegerField(blank=False)
    expire_days = models.FloatField(blank=True)
    detail = models.CharField(max_length=100)
    with_group = models.BooleanField(blank=False)
    created = models.DateTimeField(auto_created=True)
    updated = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.trip_title


class Activity(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    date = models.DateTimeField(blank=False, default=datetime.now, null=False)
    location = models.CharField(max_length=1000, blank=False, null=False)
    leader_name = models.CharField(max_length=100, blank=False, null=False)
    leader_email = models.EmailField(max_length=100,blank=True)
    leader_phone = models.CharField(max_length=100,blank=True)
    leader_lineid = models.CharField(max_length=100,blank=True)
    activity_fee = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    createby = models.CharField(blank=True, default="system", max_length=100, null=False)
    updated = models.DateTimeField(auto_created=True, auto_now_add=True)
    updateby = models.CharField(default="system", blank=True, max_length=100)

    def __str__(self):
        return self.title
