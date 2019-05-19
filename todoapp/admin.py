from django.contrib import admin
from todoapp.models import Todo
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class TodoResource(resources.ModelResource):
    class Meta:
        model = Todo
        fields = ('title','Descriptions', 'created_at', 'updated_at', 'completion_date', 'status', 'visible_status',)

@admin.register(Todo)
class TodoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = TodoResource
    list_display = ('title','Descriptions', 'created_at', 'updated_at', 'completion_date', 'status', 'visible_status',)
    list_filter = ('title', 'Descriptions', 'status', 'visible_status')
    search_fields = ('title', 'visible_status')
