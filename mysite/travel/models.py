from django.db import models

# Create your models here.


class Travels():
    travel_name = models.CharField(max_length=100)
    expire_days = models.IntegerField(default=3)
    with_group = models.BooleanField(default=True)
    amount = models.BigIntegerField(blank=False)
    strat_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    place = (
        ('TW', 'Taiwan'), ('JP', 'Japain'),
        ('US',
         'United States'), ('KR', 'Korea'), ('CH', 'China')
    )
    created = models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)
