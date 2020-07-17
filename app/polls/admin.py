from django.contrib import admin
from .models import Question, Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Date Info', {'fields': ['published_on']}),
        (None, {'fields': ['body']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
