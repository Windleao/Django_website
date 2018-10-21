from django.urls import path
from . import views #.代表当前app

urlpatters =[ #urlpatters 变量名固定
    path('',views.Hello)
]