from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('praktikum2/', praktikum2),
    path('praktikum3_1/', praktikum3_1),
    path('praktikum3_2/', praktikum3_2),
    path('praktikum3_3/', praktikum3_3),
]