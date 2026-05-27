from django.contrib import admin
from django.contrib.auth.models import User

from .models import Council, Project, Department


class CouncilAdmin(admin.ModelAdmin):
    list_display = ("name", "contact", "contact_email")
    prepopulated_fields = {"slug": ("name",)}


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "council", "budget", "created_at"]
    list_filter = ["council"]
    search_fields = ["title", "description"]


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", "council", "project"]
    list_filter = ["council", "project"]
    search_fields = ["name", "description"]


admin.site.register(Council, CouncilAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Department, DepartmentAdmin)
