
from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('search/', views.search, name='search'),
    # path('cart/', views.cart, name='cart'),
    path('about/', views.about, name='about'),
    # path('CartAdd/<int:id>', views.CartAdd, name='CartAdd'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    path('/<slug:i_slug>',views.details,name='details'),

]

