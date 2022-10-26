from django.urls import path 
from .views import UserView,UserViewDetail,LoginView, UserViewDetailDelete, UserViewDetailEdit

urlpatterns= [
    path("accounts/", UserView.as_view()),
    path("login/",LoginView.as_view()),
    path("accounts/newest/<int:num>/", UserViewDetail.as_view()),
    path("accounts/<pk>/", UserViewDetailEdit.as_view()),
    path("accounts/<pk>/management/",UserViewDetailDelete.as_view())
]