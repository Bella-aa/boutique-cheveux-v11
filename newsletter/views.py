""" Imports for model, modules and the form """
from django.shortcuts import render, redirect

from django.contrib import messages
from .forms import NewsletterUserForm


def newsletter_sign_up(request):
    """ View to store email to the database """
    form = NewsletterUserForm()
    context = {'form': form}
    if request.method == "POST":
        email_user = NewsletterUserForm(request.POST)
        email_user.save()
        print(email_user)
        messages.success(request, "Email Received. Thank You! ")
        return redirect('home')

    return render(request, "newsletter/newsletter.html", context)

