from django.core.paginator import Paginator,InvalidPage,EmptyPage
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . models import *
# Create your views here.


def home(request,c_slug=None):
    print(c_slug)
    allitems=None
    allcat=None
    if c_slug!=None:
        allcat=get_object_or_404(category,slug=c_slug)
        allitems=Items.objects.all().filter(Item_cat=allcat)
        print("hi")
    else:
        allitems=Items.objects.all()
    allcat=category.objects.all()
    paginator=Paginator(allitems,4)
    try:
        page=int(request.GET.get('page',1))
    except :
        page=1
    try:
        pageno=paginator.page(page)
    except(EmptyPage,InvalidPage):
        pageno=Paginator.page(Paginator.num_pages)

    return render(request,"index.html",{'allitems':allitems,'allcat':allcat,'pageno':pageno})
    # return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def search(request):
    item=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        print(query)
        item=Items.objects.all().filter(Q(Item_name__contains=query)|Q(Item_desc__contains=query))
        return render(request, "search.html",{'item':item,'query':query})
def details(request,i_slug):
    print("1")
    item=None
    if i_slug!=None:
        print("2")
        item=Items.objects.all().filter(Item_slug=i_slug)
        return render(request,"itemsetails.html",{'item':item})
    else:
        return render(request, "home.html")

    return render(request, "home.html")

def register(request):
    return render(request,"Register.html")
def Login(request):
    return render(request,"Login.html")
