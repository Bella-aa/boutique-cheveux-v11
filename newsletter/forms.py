""" Imports model and form """
from django import forms
from .models import NewsletterUser


class NewsletterUserForm(forms.ModelForm):
    """ Signup form """

    class Meta:
        """ Render NewsletterUser """
        model = NewsletterUser
        fields = '__all__'
