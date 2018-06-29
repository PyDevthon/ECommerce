from django.db import models
from django.contrib.auth.models import User
import random

CATEGORIES = [('SOFAS & LOUNGERS', 'SOFAS & LOUNGERS'), ('SETTEES & BENCHES', 'SETTEES & BENCHES'),
              ('ACCENT CHAIRS', 'ACCENT CHAIRS'), ('FOLDING CHAIRS', 'FOLDING CHAIRS'),
              ('PLASTIC CHAIRS', 'PLASTIC CHAIRS'), ('STOOLS', 'STOOLS'), ('BEAN BAGS', 'BEAN BAGS'),
              ('TV UNITS', 'TV UNITS'), ('DISPLAY UNITS', 'DISPLAY UNITS'), ('CABINETS', 'CABINETS'),
              ('SHOE RACKS', 'SHOE RACKS'), ('COFFEE TABLES', 'COFFEE TABLES'), ('END TABLES', 'END TABLES'),
              ('CONSOLE TABLES', 'CONSOLE TABLES'), ('DINING', 'DINING'), ('MODULAR KITCHEN', 'MODULAR KITCHEN'),
              ('BAR FURNITURE', 'BAR FURNITURE'), ('BEDS', 'BEDS'), ('MATTRESSES', 'MATTRESSES'),
              ('BEDSIDE TABLES', 'BEDSIDE TABLES'), ('CHEST OF DRAWERS', 'CHEST OF DRAWERS'),
              ('DRESSING TABLES', 'DRESSING TABLES'), ('WARDROBES', 'WARDROBES'),
              ('MODULAR WARDROBES', 'MODULAR WARDROBES'), ('KIDS FURNITURE', 'KIDS FURNITURE'),
              ('STUDY TABLES', 'STUDY TABLES'), ('BOOK SHELVES', 'BOOK SHELVES'), ('BOOK CASES', 'BOOK CASES'),
              ('FURNITURE ACCENTS', 'FURNITURE ACCENTS'), ('OFFICE FURNITURE', 'OFFICE FURNITURE'),
              ('OUTDOOR FURNITURE', 'OUTDOOR FURNITURE')]


class PlotManager(models.Manager):
    def get_categories(self):
        items = []
        for x in Product.objects.all():
            if x.category not in items:
                items.append(x.category)
        return items

    def get_count(self):
        value_count = []
        labels = self.get_categories()
        for x in labels:
            value_count.append((x, Product.objects.filter(category=x).count()))
        return value_count


class Product(models.Model):
    name = models.TextField(blank=False, null=False)
    price = models.CharField(max_length=1000, blank=False, null=False)
    description = models.TextField(null=True, blank=True)
    category = models.TextField(choices=CATEGORIES, blank=False, null=False)
    objects = PlotManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id',)


class Image(models.Model):
    name = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='static/images')
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    phone = models.CharField(max_length=10, blank=False, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    comments = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id',)


class Cart(models.Model):
    user = models.ManyToManyField(User)
    item = models.ManyToManyField(Product)
