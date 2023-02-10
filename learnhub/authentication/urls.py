from django.urls.conf import path
from .views import Registeration, Login, Logout, password_change, password_done

urlpatterns = [
    path('register/', Registeration.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('password_change/', password_change, name='password_change'),
    path('password_done/', password_done, name='password_done'),

]
