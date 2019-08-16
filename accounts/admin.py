from django.contrib import admin

from .models import Agent, ContentManager, VerificicationDocument


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ['user', 'name']


@admin.register(ContentManager)
class ContentManagerAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name']
    


admin.site.register(VerificicationDocument)