from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Poll(models.Model):
    def __unicode__(self):
        return self.question
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    date_hierarchy = 'pub_date'

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <  now


    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    def __unicode__(self):
        return self.choice_text
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)