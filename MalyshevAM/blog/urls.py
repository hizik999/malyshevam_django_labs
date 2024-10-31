from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('praktikum2/', praktikum2),
    path('praktikum3_1/', praktikum3_1),
    path('praktikum3_2/', praktikum3_2),
    path('praktikum3_3/', praktikum3_3),
    path('praktikum4_1/', praktikum4_1),
    path('praktikum4_2/', praktikum4_2),
    path('praktikum4_3/', praktikum4_3),
    path('praktikum4_4/', praktikum4_4),
    path('praktikum5/', praktikum5),
    path('praktikum6/', blog_index),
    path('praktikum7/', praktikum7),
    path('praktikum8/', praktikum8),
    path('praktikum9/', praktikum9_1),
]