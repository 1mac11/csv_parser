from django.db import models


class Product(models.Model):

    code = models.CharField(blank=True, max_length=200)
    name = models.CharField(blank=True, max_length=200)
    st1 = models.CharField(blank=True, max_length=200)
    st2 = models.CharField(blank=True, max_length=200)
    st3 = models.CharField(blank=True, max_length=200)
    price = models.CharField(blank=True, max_length=200)
    priceSP = models.CharField(blank=True, max_length=200)
    amount = models.CharField(blank=True, max_length=200)
    svoystva = models.CharField(blank=True, max_length=200)
    sovmestnie_pokupki = models.CharField(blank=True, max_length=200)
    edinitsa_izmereniya = models.CharField(blank=True, max_length=200)
    image = models.CharField(blank=True, max_length=200)
    on_main = models.CharField(blank=True, max_length=200)
    description = models.TextField(blank=True)




