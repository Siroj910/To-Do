from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    # slug = models.SlugField()

    class Meta:
        # ordering...
        ordering = ['complete']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title


    # def get_absolute_url(self):
    #     return ''