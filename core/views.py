from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm


def index(request):
    """
    Renders the home page of the site.
    """
    # Get the latest 4 unsold items
    items = Item.objects.filter(is_sold=False)[:4]
    # Get all categories
    categories = Category.objects.all()

    # Render the home page with the retrieved items and categories
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })


def contact(request):
    """
    Renders the contact page of the site.
    """
    # Render the contact page
    return render(request, 'core/contact.html')


def signup(request):
    """
    Renders the signup page and handles user signup requests.
    """
    if request.method == 'POST':
        # If the form was submitted, validate it
        form = SignupForm(request.POST)

        if form.is_valid():
            # If the form is valid, save the new user and redirect to login page
            form.save()
            return redirect('/login/')
    else:
        # If the form wasn't submitted, create a new blank form
        form = SignupForm()

    # Render the signup page with the form
    return render(request, 'core/signup.html', {
        'form': form
    })
