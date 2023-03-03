from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from item.models import Item


@login_required
def index(request):
    """
    Renders the dashboard page for the logged-in user.
    """
    # Get all items created by the current user
    items = Item.objects.filter(created_by=request.user)

    # Render the dashboard page with the retrieved items
    return render(request, 'dashboard/index.html', {
        'items': items,
    })
