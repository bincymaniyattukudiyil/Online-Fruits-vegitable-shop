
from django.urls import path

from . import views

urlpatterns=[

    path('cart/', views.cart, name='cart'),
    path('CartAdd/<int:id>', views.CartAdd, name='CartAdd'),
    path('CartDelete/<int:id>', views.CartDelete, name='CartDelete'),
    path('CartRemove/<int:id>', views.CartRemove, name='CartRemove'),

    path('CartIncrement/<int:id>', views.CartIncrement, name='CartIncrement'),

]

