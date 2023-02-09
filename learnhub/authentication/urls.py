from django.urls.conf import path
from .views import Registeration

urlpatterns = [
    path('register/', Registeration.as_view(), name='register')
]
