from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #User who wrote the story.
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    

class StoryChapter(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    content = models.TextField()
    parent_node = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='child_nodes')
    choice_text = models.CharField(max_length=100, blank=True, null=True)
    chapter_number = models.PositiveIntegerField(editable=False, default=1)

    def save(self, *args, **kwargs):
        if not self.pk:
            max_chapter = StoryChapter.objects.filter(story=self.story).aggregate(max_chapter_number=models.Max('chapter_number'))
            self.chapter_number = (max_chapter['max_chapter_number'] or 0) + 1

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Chapter {self.chapter_number} of Story {self.story.pk}: {self.story.title}"

class Interaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    #User who is reading or interacting with the story.
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    current_node = models.ForeignKey(StoryChapter, on_delete=models.CASCADE)
    time_spent = models.DurationField(null=True, blank=True)
    choice_made = models.ForeignKey(StoryChapter, related_name='choices_made', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.username} is reading {self.story.title} story."