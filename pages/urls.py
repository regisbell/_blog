from django.urls import path
from . import views HomePageView, AboutPageView

urlpatterns = [
    path('home/', HomePageView.as_view(), name = 'home'),
    path('about/', AboutPageView.as_view(), name = 'about'),
]
