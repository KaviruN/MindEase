from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birthday', 'gender')
    search_fields = ('user__username', 'birthday', 'gender')
    list_filter = ('birthday', 'gender')

admin.site.register(UserProfile, UserProfileAdmin)