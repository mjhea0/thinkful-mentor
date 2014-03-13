from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# Register your models here.
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question', {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    
admin.site.register(Poll, PollAdmin)

