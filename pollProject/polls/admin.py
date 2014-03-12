from django.contrib import admin
from polls.models import Choice, Poll

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    list_display = ('question', 'pub_date')
    search_fields = ['question']

admin.site.register(Poll, PollAdmin)
