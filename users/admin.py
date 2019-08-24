from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["username", "email"]
    # fieldsets = (
    #     (
    #         ("General Info"),
    #         {
    #             "fields": (
    #                 "username",
    #                 "password",
    #                 "workplace",
    #                 "contributor"
    #             )
    #         }
    #     ),
    #     (
    #         _("Personal Info"),
    #         {
    #             "fields": (
    #                 "first_name",
    #                 "last_name",
    #                 "email"
    #             )
    #         }
    #     ),
    #     (
    #         _("Permissions"),
    #         {
    #             "fields": (
    #                 "is_active",
    #                 "is_staff",
    #                 "is_superuser",
    #                 "groups",
    #                 "user_permissions",
    #             )
    #         },
    #     ),
    #     (
    #         _("Important dates"),
    #         {
    #             "fields": (
    #                 "last_login",
    #                 "date_joined"
    #             )
    #         }
    #     ),
    # )

admin.site.register(CustomUser, CustomUserAdmin)
