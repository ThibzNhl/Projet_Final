from django.contrib import admin
from .models import Pipeline, Step, Task


admin.site.register(Step)
@admin.register(Pipeline)
class PipelineAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'last_run')

admin.site.register(Task)