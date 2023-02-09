from django.urls.conf import path
from .views import Registeration, Login

urlpatterns = [
    path('register/', Registeration.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
]
