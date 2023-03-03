from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewItemForm, EditItemForm
from .models import Category, Item

def items(request):
    """
    Renders the items page and handles item search requests.
    """
    # Get the search query and selected category (if any)
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)

    # Get all categories and all unsold items
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    # Filter items by selected category and search query (if any)
    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    # Render the items page with the retrieved items, query, and categories
    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })


def detail(request, pk):
    """
    Renders the detail page for a specific item.
    """
    # Get the item with the given primary key
    item = get_object_or_404(Item, pk=pk)
    # Get up to 3 related unsold items in the same category (excluding the current item)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    # Render the detail page with the retrieved item and related items
    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })


@login_required
def new(request):
    """
    Renders the new item page and handles new item requests.
    """
    if request.method == 'POST':
        # If the form was submitted, validate it
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            # If the form is valid, create a new item and save it
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        # If the form wasn't submitted, create a new blank form
        form = NewItemForm()

    # Render the new item page with the form
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })


@login_required
def edit(request, pk):
    """
    Renders the edit item page and handles edit item requests.
    """
    # Get the item with the given primary key and created by the current user
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        # If the form was submitted, validate it
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            # If the form is valid, save the edited item
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        # If the form wasn't submitted, pre-populate it with the item data
        form = EditItemForm(instance=item)

    # Render the edit item page with the form
    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })

@login_required
def delete(request, pk):
    """
    Handles delete item requests.
    """
    # Get the item with the given primary key and created by the current user
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    # Delete the item
    item.delete()
    return redirect('dashboard:index')
