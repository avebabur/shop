from django.db import models
from ckeditor import fields
from django.contrib.auth.models import User


class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description =  fields.RichTextField()
    inStock = models.BooleanField(default=False, blank=True)
    image = models.ImageField(upload_to='Uploads')
    rubric = models.ForeignKey('Rubric', on_delete=models.PROTECT)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def average_rating(self):
        return Rating.objects.filter(product=self).aggregate(Avg('rating'))['rating_avg'] or 0

    class Meta:
        ordering = ['-created']
class Rubric(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Uploads')

    def __str__(self):
        return self.name

class Comments(models.Model):
    RATING_CHOICES = (
        ('1', 'very bad'),
        ('2', 'bad'),
        ('3', 'ok'),
        ('4', 'good'),
        ('5', 'excellent')
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    comment = models.TextField()
    rating = models.CharField(max_length=100, choices=RATING_CHOICES)