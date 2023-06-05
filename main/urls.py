from django.urls import path


from main import views
from main.api import MovieAPIView

urlpatterns = [
    #pages
    path('show',views.show,name='movies'),
    #API
    path('',MovieAPIView.as_view()),
]