from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAdminOrReadOnly, IsUserOwnerOrAdmin
from users.serializers import UserSerializer
from .models import User


# Create your views here.

class UserView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, 201)


class UserOwnerView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserOwnerOrAdmin]

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)

        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)

        return Response(serializer.data, 200)

    def patch(self, request, user_id):

        user = get_object_or_404(User, id=user_id)

        self.check_object_permissions(request, user)
        serializer = UserSerializer(user, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, 200)
