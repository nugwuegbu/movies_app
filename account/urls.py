from django.contrib.auth.views import LogoutView
from django.urls import path
from account.views import AccountLoginView

urlpatterns = [
    path('',AccountLoginView.as_view(),name='login'),
    path('logout',LogoutView.as_view(next_page='login'),name="logout"),
]