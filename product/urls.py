from django.urls import path 
from .views import ProductView, ProductViewDetail

urlpatterns= [
    path("", ProductView.as_view()),
    path("<pk>/",ProductViewDetail.as_view()),

]