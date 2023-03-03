from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item
from .forms import ConversationMessageForm
from .models import Conversation


@login_required
def new_conversation(request, item_pk):
    """
    Renders the new conversation page and handles new conversation requests.
    """
    # Get the item with the given primary key
    item = get_object_or_404(Item, pk=item_pk)

    # If the current user created the item, redirect to the dashboard
    if item.created_by == request.user:
        return redirect('dashboard:index')

    # Check if a conversation with the item already exists
    existing_conversation = Conversation.objects.filter(item=item, members=request.user).first()

    if existing_conversation:
        # If a conversation already exists, redirect to its detail page
        return redirect('conversation:detail', pk=existing_conversation.id)

    if request.method == 'POST':
        # If the form was submitted, validate it
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            # If the form is valid, create a new conversation and save the message
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk=item_pk)
    else:
        # If the form wasn't submitted, create a new blank form
        form = ConversationMessageForm()

    # Render the new conversation page with the form
    return render(request, 'conversation/new.html', {
        'form': form
    })


@login_required
def inbox(request):
    """
    Renders the inbox page for the logged-in user.
    """
    # Get all conversations involving the current user
    conversations = Conversation.objects.filter(members__in=[request.user.id]).prefetch_related('members')

    # Render the inbox page with the retrieved conversations
    return render(request, 'conversation/inbox.html', {
        'conversations': conversations
    })


@login_required
def detail(request, pk):
    """
    Renders the detail page for a specific conversation and handles new message requests.
    """
    # Get the conversation with the given primary key and involving the current user
    conversation = get_object_or_404(Conversation, pk=pk, members=request.user)

    if request.method == 'POST':
        # If the form was submitted, validate it
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            # If the form is valid, save the new message and the conversation
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('conversation:detail', pk=pk)
    else:
        # If the form wasn't submitted, create a new blank form
        form = ConversationMessageForm()

    # Render the detail page with the conversation and the form
    return render(request, 'conversation/detail.html', {
        'conversation': conversation,
        'form': form
    })
