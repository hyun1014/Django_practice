from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=100, blank=True)
    url = models.URLField(verbose_name='URL', unique=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title
        