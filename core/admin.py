from django.contrib import admin
from django.contrib.admin.models import LogEntry

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['action_time', 'user', 'content_type', 'object_repr', 'action_flag']
    list_filter = ['action_time', 'user', 'action_flag']
    search_fields = ['object_repr', 'change_message']
    readonly_fields = [f.name for f in LogEntry._meta.get_fields()]
    list_per_page = 20 # Request #4: Pagination
    
    def has_add_permission(self, request):
        return False
        
    def has_change_permission(self, request, obj=None):
        return False
        
    def has_delete_permission(self, request, obj=None):
        return False

# Proxy model to change the display name in the admin sidebar if needed
# But usually verbose_name on the Admin class or Model works.
# Since LogEntry is a built-in model, we can't easily change its Meta without a proxy.
class RecentAction(LogEntry):
    class Meta:
        proxy = True
        verbose_name = "Recent Action"
        verbose_name_plural = "Recent Actions"

# Unregister original and register proxy
admin.site.unregister(LogEntry)
admin.site.register(RecentAction, LogEntryAdmin)
