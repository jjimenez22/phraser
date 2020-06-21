from django.db import models

# Create your models here.

class Phrase(models.Model):
    text = models.CharField(max_length=250)
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
