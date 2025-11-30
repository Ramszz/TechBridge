from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ("Extra", {"fields": ("role", "branch", "year", "company", "headline", "skills")}),
    )
    list_display = ("username", "email", "role", "company")

admin.site.register(CustomUser, CustomUserAdmin)
