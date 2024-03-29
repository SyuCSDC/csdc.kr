from django.contrib import admin
from .models import Report, Book , ReportFile

# Register your models here.

# ReportFile 모델을 인라인으로 표시하기 위한 클래스
class ReportFileInline(admin.TabularInline):
    model = ReportFile
    extra = 1  # 기본적으로 표시할 빈 폼의 수

# Report 모델을 관리자 페이지에 등록
class ReportAdmin(admin.ModelAdmin):
    list_display = ('book', 'submitter')
    search_fields = ('book__title', 'submitter__username' )
    inlines = [ReportFileInline] 
    
# Book 모델을 관리자 페이지에 등록
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_requester_username', 'get_requester_full_name', 'needed_copies')
    search_fields = ('title', 'author', 'requester__username')

    def get_requester_username(self, obj):
        return obj.requester.username
    get_requester_username.short_description = 'Requester Username'

    def get_requester_full_name(self, obj):
        return obj.requester.get_full_name() if obj.requester.get_full_name() else 'N/A'
    get_requester_full_name.short_description = 'Requester Full Name'


admin.site.register(Report, ReportAdmin)
admin.site.register(Book, BookAdmin)