from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


from rest_framework.exceptions import AuthenticationFailed

from project_app.models import User
from project_app.serializers import UserSerializer


# Create your views here.

class Register(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.filter().first()
        refresh_token = RefreshToken.for_user(user)

        return Response({
            "success": True,
            "message": "Successfull",
            "refresh": str(refresh_token),
            "access": str(refresh_token.access_token)
        })


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed("User not registring")
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')

        refresh_token = RefreshToken.for_user(user)

        return Response({
            "success": True,
            "message": "Successfull",
            "refresh": str(refresh_token),
            "access": str(refresh_token.access_token)
        })

