from django.urls import path
from .views import *

urlpatterns = [
    path('', appointment, name='appointment'),
    # path('index2/', index2, name='index2'),
    path('docshowbydept/', docshowbydept, name='docshowbydept'),
    path('docshowbydept2/', docshowbydept2, name='docshowbydept2'),
    path('docshowbydept3/', docshowbydept3, name='docshowbydept3'),
    path('docshowbydept4/', docshowbydept4, name='docshowbydept4'),
]