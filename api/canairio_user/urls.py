# The Django project also has a urls.py file.
# Add a reference to your application's urls.py file.
# Add the URL patterns.

from django.urls import path

from . import views

urlpatterns = [
    path('v1/canairio-user', views.CanairioUserView.as_view(), name='canairio-user'),
]
