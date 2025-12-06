from django.contrib import admin
from .models import Task, Subtask


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'priority', 'status', 'due_date', 'created_at')
    list_filter = ('priority', 'status', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Subtask)
class SubtaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title',)

