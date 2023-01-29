from django.core.paginator import Paginator,InvalidPage,EmptyPage
from django.db.models import Q
from django.http import HttpResponse
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from shop.models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def CartId(request):
    C_id=request.session.session_key
    if not C_id:
        C_id=request.session.create()
    return C_id
def cart(request,tot=0,count=0,c_item=None):
    c_id = CartId(request)
    c_item=Cart.objects.filter(C_id=c_id)
    for i in c_item:
        tot +=(i.c_qty*i.Item_id.Item_price)
        count +=i.c_qty
    return render(request,"cart.html",{'c_item':c_item,'tot':tot,'count':count})


def CartAdd(request,id):
    c_id=CartId(request)
    item_id=Items.objects.get(id=id)
    try:
        c_items = Cart.objects.get(C_id=c_id,Item_id=item_id)
        if c_items.c_qty>=1:
            c_items.c_qty+=1
        c_items.save()
    except Cart.DoesNotExist:
        c_items = Cart.objects.create(Item_id=item_id, c_qty=1, C_id=c_id)
        c_items.save()
    return redirect('cart')

def CartRemove(request,id):
    c_id = CartId(request)
    # item_id = Items.objects.get(id=id)
    c_items = Cart.objects.get(C_id=c_id, id=id)
    if c_items.c_qty>1:
        c_items.c_qty -=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cart')
    # return render(request, "cart.html")
def CartIncrement(request,id):
    c_id = CartId(request)
    # item_id = Items.objects.get(id=id)
    c_items = Cart.objects.get(C_id=c_id, id=id)
    if c_items.c_qty>1:
        c_items.c_qty +=1
        c_items.save()
    else:
        c_items.delete()
    # return render(request, "cart.html")
    return redirect('cart')
def CartDelete(request,id):
    c_id = CartId(request)
    # item_id = Items.objects.get(id=id)
    c_items = Cart.objects.get(C_id=c_id,id=id)
    c_items.delete()
    # return render(request, "cart.html")
    return redirect('cart')
    # pass

