from django.urls import path
from .views import *
 
urlpatterns = [
    ### praktikums
    #path('', index),
    path('praktikum2/', praktikum2),
    path('praktikum3_1/', praktikum3_1),
    path('praktikum3_2/', praktikum3_2),
    path('praktikum3_3/', praktikum3_3),
    path('praktikum4_1/', praktikum4_1),
    path('praktikum4_2/', praktikum4_2),
    path('praktikum4_3/', praktikum4_3),
    path('praktikum4_4/', praktikum4_4),
    path('praktikum5/', praktikum5),
    path('praktikum7/', praktikum7),
    path('praktikum8/', praktikum8),
    path('praktikum9_1/', praktikum9_1),
    path('praktikum9_2/', praktikum9_2),
    path('praktikum9_3/', praktikum9_3),
    path('praktikum9_4/', praktikum9_4),

    ### Blog
    #path('', Home.as_view(), name='home'),
    path('blog/', Home.as_view(), name='home'),
    path('category/<slug:slug>', PostsByCategory.as_view(), name='category'),
    path('post/<slug:slug>', GetPost.as_view(), name='post'),
    path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
]