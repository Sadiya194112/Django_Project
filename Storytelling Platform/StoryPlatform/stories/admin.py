from django.contrib import admin
from .models import Story, StoryChapter, Interaction

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'author', 'created_at')
    search_fields = ('title', 'description', 'author__username')

@admin.register(StoryChapter)
class StoryChapterAdmin(admin.ModelAdmin):
    list_display = ('id','story', 'parent_node', 'choice_text')
    search_fields = ('story__title', 'choice_text')

@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'story', 'current_node', 'time_spent', 'choice_made')
    search_fields = ('user__username', 'story__title', 'current_node__story__title', 'choice_made__story__title')
