from django.contrib import admin
from .models import Inquiry

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['name', 'email', 'phone', 'message']
    readonly_fields = ['name', 'email', 'phone', 'subject', 'message', 'created_at']
    list_per_page = 20
    
    fields = ['name', 'email', 'phone', 'subject', 'message', 'status', 'created_at']
