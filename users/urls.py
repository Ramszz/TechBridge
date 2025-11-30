from django.urls import path
from .views import (
    RegisterView, ProfileView, UserListView,
    AlumniListView, StudentListView,
    AdminUserListView, AdminUserDetailView
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="user-register"),
    path("me/", ProfileView.as_view(), name="user-profile"),
    path("list/", UserListView.as_view(), name="user-list"),

    # public directories
    path("alumni/", AlumniListView.as_view(), name="alumni-list"),
    path("students/", StudentListView.as_view(), name="student-list"),

    # admin management (admin-only)
    path("manage/", AdminUserListView.as_view(), name="admin-user-list"),
    path("manage/<str:username>/", AdminUserDetailView.as_view(), name="admin-user-detail"),
]
