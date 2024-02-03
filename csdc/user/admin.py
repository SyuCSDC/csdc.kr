# Register your models here.
from django.contrib import admin
from .models import UserProfile

# UserProfile 모델을 관리자 페이지에 등록
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'grade', 'student_id', 'role', 'bio')
    search_fields = ('user__username', 'student_id', 'role')

admin.site.register(UserProfile, UserProfileAdmin)
