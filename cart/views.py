from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from events.models import EventInstance
# Create your views here.

def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified event to the shopping cart """
    event = EventInstance.objects.get(pk=item_id)
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    which_athlete = request.POST.get('which_athlete')
    print(which_athlete)
    cart = request.session.get('cart', {})

    
    if item_id in list(cart.keys()):
        if which_athlete in cart[item_id]['items_by_athlete'].keys():
            # Add error here to refuse to add another entry for the same athlete
            # cart[item_id]['items_by_athlete'][which_athlete] += quantity
            print (which_athlete)
        else:
            cart[item_id]['items_by_athlete'][which_athlete] = quantity
    else:
        cart[item_id] = {'items_by_athlete': {which_athlete: quantity}}
        messages.success(request, f'{which_athlete} is ready to enter the {event.friendlyname}.')


    # if item_id in list(cart.keys()):
     #   cart[item_id] += quantity
    #else:
    #    cart[item_id] = quantity

    request.session['cart'] = cart

    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""
    test = request.POST['which_athlete']
    print(test)
    try:
        which_athlete = None
        if 'which_athlete' in request.POST:
            athlete = request.POST['which_athlete']
        cart = request.session.get('cart', {})
        print (cart)

        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)