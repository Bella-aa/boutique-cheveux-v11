""" Import models """
from django.db import models


class NewsletterUser(models.Model):
    """ Newsletter model """
    email_user = models.EmailField(blank=True)

    def __str__(self):
        """ Email addresse method """
        return self.email_user
