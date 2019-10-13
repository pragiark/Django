from django.db import models

class Topic(models.Model):
    """"User Topic"""
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)

def __str__(self):
    """Return presentation of models"""
    return self.text