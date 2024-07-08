from django.contrib import admin
from join.models import Board, TaskCategory, Task

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')
    filter_horizontal = ('users',) 


class TaskCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'color')


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'priority', 'due_date', 'board')
    filter_horizontal = ('users',)  


admin.site.register(Task, TaskAdmin)

admin.site.register(Board, BoardAdmin)

admin.site.register(TaskCategory, TaskCategoryAdmin)

