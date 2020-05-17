from django.contrib import admin
from .models import Bookmark

# Register your models here.

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'url', 'tag_list']
    fieldsets = (
        ('Info', {
            "fields": (
                'title', 'url','tags',
            ),
        }),
    )

    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tags.all())
    
#admin.site.register(Bookmark, BookmarkAdmin)