from rest_framework.authtoken import views
from rest_framework.urls import url
from .views import RegisterUser,ShowProfile

urlpatterns = [
    url('register',RegisterUser.as_view(),name='register'),
    url('login' , views.obtain_auth_token , name='login'),
    url('myprofile' , ShowProfile.as_view(), name='profile')
]