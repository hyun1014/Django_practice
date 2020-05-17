from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name='Post_Title', max_length=100, default="Empty title", blank=True)
    slug = models.SlugField(verbose_name='SLUG', unique=True, allow_unicode=True,\
        help_text='one word for title alias.')
    description = models.CharField(verbose_name='Description', max_length=100, blank=True, help_text= 'simple \
        description text.')
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFIED DATE', auto_now=False)
    tags = TaggableManager()

    class Meta:
        verbose_name = 'posting'
        verbose_name_plural = 'postings'
        db_table = 'blog_posts'
        ordering = ('-modify_dt',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", args=(self.slug,))

    def get_previous(self):
        return self.get_previous_by_modify_dt()
    
    def get_next(self):
        return self.get_next_by_modify_dt()
    