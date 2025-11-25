from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from admision_api.core.serializers.auth import LoginSerializer, UserSerializer, RegisterSerializer
from admision_api.core.permissions import IsAdminUser


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """
    Endpoint de login que retorna tokens JWT y datos del usuario
    """
    serializer = LoginSerializer(data=request.data)
    
    if serializer.is_valid():
        user = serializer.validated_data['user']
        
        # Generar tokens JWT
        refresh = RefreshToken.for_user(user)
        
        # Serializar datos del usuario
        user_serializer = UserSerializer(user)
        
        return Response({
            'message': 'Login exitoso',
            'user': user_serializer.data,
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        }, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def logout_view(request):
    """
    Endpoint de logout (opcional, ya que JWT es stateless)
    """
    try:
        refresh_token = request.data.get('refresh')
        if refresh_token:
            token = RefreshToken(refresh_token)
            token.blacklist()
        
        return Response({
            'message': 'Logout exitoso'
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'error': 'Token inválido'
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    """
    Endpoint para registrar nuevos usuarios.
    Por defecto crea usuarios normales (is_staff=False).
    Solo administradores pueden crear otros administradores.
    """
    serializer = RegisterSerializer(data=request.data)
    
    if serializer.is_valid():
        # Verificar si se intenta crear un administrador
        is_admin = request.data.get('is_admin', False)
        
        if is_admin and not (request.user.is_authenticated and request.user.is_staff):
            return Response({
                'error': 'Solo los administradores pueden crear usuarios administradores'
            }, status=status.HTTP_403_FORBIDDEN)
        
        user = serializer.save()
        
        # Generar tokens JWT para auto-login
        refresh = RefreshToken.for_user(user)
        user_serializer = UserSerializer(user)
        
        return Response({
            'message': 'Usuario registrado exitosamente',
            'user': user_serializer.data,
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile_view(request):
   
    serializer = UserSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)
