from django.urls import path
from .views import SignUpFormView,LoginFormView,LogoutFormView
from . import views
urlpatterns = [
    path('sign_up/',SignUpFormView.as_view(), name = 'signUp'),
    path('profile/',views.ProfileView, name = 'profile'),
    path('login/',LoginFormView.as_view(), name = 'login'),
    path('logout/',LogoutFormView.as_view(), name = 'logout'),
   

]