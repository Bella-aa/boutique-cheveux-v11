from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Product, Review
from .forms import ReviewForm


def products(request):
    """ Render products """
    products_all = Product.objects.all()
    context = {
        'products_all': products_all,
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def create_review(request, pk):
    """ Creating a review """
    form = ReviewForm(initial={'product_reviewed': pk, 'user_reviewing': request.user})
    product = get_object_or_404(Product, pk=pk)
    context = {
        'form': form,
        'product': product,
    }
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=pk)

    return render(request, 'review/review.html', context)


@login_required
def update_review(request, pk):
    """ A view to update review """
    review = Review.objects.get(pk=pk)
    form = ReviewForm(instance=review)
    product_id = review.product_reviewed.id

    context = {
        'form': form,
        'review': review,
        'product_id': product_id
    }
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return HttpResponseRedirect(reverse('product_detail', kwargs={'product_id': product_id}))

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated review!')
            return HttpResponseRedirect(reverse('product_detail', kwargs={'product_id': product_id}))
        else:
            messages.error(request, 'Failed to update review. Please ensure the form is valid.')
    messages.info(request, f'You are editing {review.title}')
    return render(request, 'review/update_review.html', context)


@login_required
def delete_review(request, pk):
    """ A view to delete reviews """
    review = Review.objects.get(id=pk)
    form = ReviewForm(instance=review)
    product_id = review.product_reviewed.id
    context = {
        'form': form,
        'item': review,
        'product_id': product_id
    }
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return HttpResponseRedirect(reverse('product_detail', kwargs={'product_id': product_id}))

    if request.method == 'POST':
        review.delete()
        return HttpResponseRedirect(reverse('product_detail', kwargs={'product_id': product_id}))

    return render(request, 'review/delete_review.html', context)
