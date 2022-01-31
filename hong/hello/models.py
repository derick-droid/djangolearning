# from pyexpat import model
from django.db import models
# from pytz import timezone

# Create your models here.

class Questionpolls(models.Model):
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField('publication date')
    
    
    def __str__(self):
        return self.question_text
