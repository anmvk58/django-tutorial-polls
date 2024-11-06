from django.contrib import admin

from polls.models import Question, Choice

# Register your models here.

# admin.site.register(Question)
admin.site.register(Choice)

# Method 1 (simplest)
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ["pub_date", "question_text"]


# Method 2
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ("Content information", {"fields": ["question_text"]}),
#         ("Date information", {"fields": ["pub_date"]}),
#     ]

# Method 3
# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)