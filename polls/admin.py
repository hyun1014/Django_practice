from django.contrib import admin
from .models import Question, Choice

class ChoiceAdmin(admin.ModelAdmin):
    fields = ['question', 'choice_text', 'vote_cnt']


class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date published', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInLine]


# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)