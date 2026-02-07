from django.contrib import admin
from .models import Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ['image', 'is_primary']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'completed_date', 'is_active']
    list_filter = ['is_active', 'completed_date']
    search_fields = ['title', 'summary', 'location']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'is_active')
        }),
        ('Project Details', {
            'fields': ('summary', 'description', 'location', 'completed_date')
        }),
    )
