from django.contrib import admin

# Register your models here.
from .models import Mentorship

# Mentorship 모델을 관리자 페이지에 등록
class MentorshipAdmin(admin.ModelAdmin):
    list_display = ('mentor', 'mentee', 'start_date', 'end_date', 'status')
    search_fields = ('mentor__username', 'mentee__username', 'status')
    list_filter = ('status', 'start_date')

admin.site.register(Mentorship, MentorshipAdmin)