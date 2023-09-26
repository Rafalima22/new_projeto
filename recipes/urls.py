
from django.urls import path

from recipes.views import contato, email, home, sobre

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
    path('email/', email),

]
