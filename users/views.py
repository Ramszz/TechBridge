from django.db.models import Q
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, RegisterSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    """
    POST /api/users/register/  -> register a student or alumni
    """
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

class ProfileView(generics.RetrieveUpdateAPIView):
    """
    GET /api/users/me/   -> view current user's profile
    PUT/PATCH /api/users/me/ -> update profile
    """
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user

class UserListView(generics.ListAPIView):
    """
    GET /api/users/list/  -> list all users (token required)
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

class AlumniListView(generics.ListAPIView):
    """
    GET /api/users/alumni/  -> public alumni directory with filters.
    """
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        qs = User.objects.filter(role="alumni")
        branch = self.request.query_params.get("branch", None)
        if branch:
            qs = qs.filter(branch__iexact=branch)
        username = self.request.query_params.get("username", None)
        if username:
            qs = qs.filter(username__iexact=username)
        q = self.request.query_params.get("q", None)
        if q:
            q = q.strip()
            qs = qs.filter(
                Q(username__icontains=q) |
                Q(first_name__icontains=q) |
                Q(last_name__icontains=q) |
                Q(skills__icontains=q)
            )
        return qs.order_by("-id")

class StudentListView(generics.ListAPIView):
    """
    GET /api/users/students/  -> public student directory (or used by admin/frontend)
    """
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        qs = User.objects.filter(role="student")
        branch = self.request.query_params.get("branch", None)
        if branch:
            qs = qs.filter(branch__iexact=branch)
        username = self.request.query_params.get("username", None)
        if username:
            qs = qs.filter(username__iexact=username)
        q = self.request.query_params.get("q", None)
        if q:
            q = q.strip()
            qs = qs.filter(
                Q(username__icontains=q) |
                Q(first_name__icontains=q) |
                Q(last_name__icontains=q) |
                Q(skills__icontains=q)
            )
        return qs.order_by("-id")

# --- Admin management endpoints (superuser only) ---

class AdminUserListView(generics.ListAPIView):
    """
    GET /api/users/manage/ -> list ALL users (admin-only)
    """
    queryset = User.objects.all().order_by("-id")
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

class AdminUserDetailView(APIView):
    """
    GET / PATCH / DELETE /api/users/manage/<username>/ -> admin-only single-user actions
    """
    permission_classes = (IsAdminUser,)

    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    def get(self, request, username):
        user = self.get_object(username)
        if not user:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def patch(self, request, username):
        user = self.get_object(username)
        if not user:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username):
        user = self.get_object(username)
        if not user:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response({"detail": "User deleted."}, status=status.HTTP_200_OK)
