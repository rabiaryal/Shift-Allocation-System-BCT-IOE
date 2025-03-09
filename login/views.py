from django.shortcuts import render
from rest_framework import generics, status
from .models import *
from .serializers import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated



class RegisterView(generics.CreateAPIView):
    queryset = HRManager.objects.all()
    serializer_class = RegisterSerializer   


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer   

    def get(self, request):
        # Fetch all HRManagers
        query_set = HRManager.objects.all()
        serializer = HRManagerSerializer(query_set, many=True)
        return Response({
            'data': serializer.data,
            'status': True
        })


    def post(self, request, *args, **kwargs):
        ManagerID = request.data.get('ManagerID')
        password = request.data.get('password')
        user = authenticate(ManagerID=ManagerID, password=password)
        
        try:
            user = HRManager.objects.get(ManagerID= ManagerID)
        except HRManager.DoesNotExist:
            return Response({
                'message': 'Invalid email or password',
                'status': False
            }, status=401)

        if check_password(password, user.password):  # ✅ Manually check hashed password
            refresh = RefreshToken.for_user(user)
            user_serializer = HRManagerSerializer(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': user_serializer.data,
                'status': True
            })
        else:
            return Response({
                'message': 'Invalid email or password',
                'status': False
            }, status=401)

class LogoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            if not refresh_token:
                return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()  # Blacklist the refresh token

            return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST) 
        

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]  # Requires authentication

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Password changed successfully!"}, status=status.HTTP_200_OK)



class ResetPasswordView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": "Password reset successfully. You can now log in with your new password."}, status=status.HTTP_200_OK)