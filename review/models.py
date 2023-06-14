from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):
    """ Comment Review model """
    title = models.CharField(max_length=150, blank=False, null=True)
    content = models.CharField(max_length=500, blank=False, null=True)
    product_reviewed = models.ForeignKey(
        Product, related_name='product_reviewed', on_delete=models.CASCADE
        )
    user_reviewing = models.ForeignKey(
        User, related_name='user_reviewing', on_delete=models.CASCADE
        )
    rating = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title
