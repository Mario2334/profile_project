from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from userprofile.models import User
from .serializers import UserSerializer
# Create your views here.


class RegisterUser(CreateAPIView):
    serializer_class = UserSerializer
    authentication_classes = ()


class ShowProfile(RetrieveAPIView):
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)

    def get_object(self):
        return get_object_or_404(User,id = self.request.user.id)

