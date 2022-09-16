""""TODO"""
import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


# Create your models here.

class Book(models.Model):
    """TODO"""
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        """TODO"""
        return self.title

    def get_absolute_url(self):
        """TODO"""
        return reverse('book_detail', kwargs={'pk':str(self.id)})


class Review(models.Model):
    """TODO"""
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews',)
    review = models.CharField(max_length=255)
    author=models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self):
        """TODO"""
        return self.review