from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('showtable',views.showtable, name="showtable"),
    path('adminpanel',views.adminpanel, name="adminpanel"),

]
