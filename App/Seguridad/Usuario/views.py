from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .Serializer import LoginSerializer, UserCreateSerializer
from .models import User
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema


class UserCreateView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Usuario creado correctamente"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUView(APIView):
    permission_classes = [AllowAny]  # 🔑 permite acceso público

    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        pais = serializer.validated_data['pais']  # solo devolvemos al frontend

        # Autenticar usuario
        user = authenticate(username=username, password=password)

        if user is None:
            return Response({"error": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

        # Definir rol según tu estructura
        rol = "Administrador" if user.is_superuser or user.is_staff else "Bodeguero"

        # Respuesta final al frontend
        return Response({
            "message": "Login exitoso",
            "username": user.username,
            
            "pais": pais  # solo devolvemos lo que envió el usuario
        }, status=status.HTTP_200_OK)