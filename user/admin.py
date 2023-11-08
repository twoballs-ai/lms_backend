from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth.models import Group


from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Student, Teacher, Manager


# class CustomStudentAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ("email", "is_active")
#     list_filter = ("email", "is_active")
#     fieldsets = (
#         (None, {"fields": ("email", "password","student_image","interested_categories")}),
#         # ("Permissions", {"fields": ("is_staff", "is_active",
#         #                             "groups", "user_permissions")}),
#     )
#     add_fieldsets = (
#         (None, {
#             "classes": ("wide",),
#             "fields": (
#                 "email","student_image","interested_categories","password1","password2"
#             )}
#         ),
#     )
#     search_fields = ("email",)
#     ordering = ("email",)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "is_student", "is_teacher", "is_active")
    list_filter = ("email", "is_student", "is_teacher", "is_active")
    fieldsets = (
        (None, {"fields": ("email","is_student", "is_teacher", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active",
                                    "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active",  "is_student", "is_teacher", 
                "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Student)
# admin.site.unregister(Group)
admin.site.register(Teacher)
admin.site.register(Manager)
# admin.site.register(Role)                 