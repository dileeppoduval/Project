from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.myfunction,name='home'),
    path('home2',views.myfunction2,name='home2'),
    path('home3',views.myfunction3,name='home3'),
    path("testpage",views.myfunctiontest,name='testpage')
]
