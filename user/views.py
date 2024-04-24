from random import randint

from django.contrib.auth import get_user_model, logout
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password

from .serializers import UserSerializer, ChangePasswordSerializer, PasswordResetSerializer
from config.settings import emails_list
from config.settings import EMAIL_HOST_USER


class RegisterUserView(CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()


@api_view(['POST'])
def send_email(request):
    if request.method == 'POST':
        email = request.data['email']
        user = get_user_model()
        if user.objects.filter(email=email).exists():
            num = randint(10000, 100000)
            emails_list[email] = num
            send_mail(
                subject='Code to reset password',
                message=f'Your code is {num}',
                from_email=EMAIL_HOST_USER,
                recipient_list=[email]
            )
            return Response({'Email is sent'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'This email is not registered'}, status=200)


@api_view(['POST'])
def password_reset(request):
    serializer = PasswordResetSerializer(data=request.data)
    code = request.data['code']
    email = request.data['email']
    password = request.data['password']
    password2 = request.data['password2']
    if password == password2:
        if code == emails_list[email]:
            user = get_user_model().objects.get(email=email)
            user.set_password(password)
            user.save()
            del emails_list[email]
            return Response({'Password has been reset.'}, status=status.HTTP_200_OK)
        else: return Response({'error': 'Wrong email or password'}, status=200)
    else:
        return Response({'error': 'Passwords do not match'}, status=200)


class ChangePasswordView(APIView):
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            old_password = serializer.validated_data.get('old_password')
            new_password = serializer.validated_data.get('new_password')
            if not check_password(old_password, user.password):
                return Response({'error': 'Incorrect old password'}, status=400)
            user.set_password(new_password)
            user.save()
            return Response({'success': 'Password changed successfully'}, status=200)
        return Response(serializer.errors, status=400)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)