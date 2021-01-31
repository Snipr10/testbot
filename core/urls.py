from django.contrib.auth.decorators import login_required
from django.urls import path

from core import views

urlpatterns = [
    # path('get_username', get_username),
    # path('leave', leave),
    path('users', views.AllUsers.as_view()),
    path('leave', views.Leave.as_view()),

]
