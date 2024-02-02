from django.contrib import admin
from .models import Profile, Book, Mentorship, Report
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user' , 'is_mentor' , 'department')

    def user_info(self , obj):
        return obj.user.username
    
    user_info.short_desciption = 'Username'

admin.site.register(Profile , ProfileAdmin)
admin.site.register(Book)
admin.site.register(Mentorship)
admin.site.register(Report)

