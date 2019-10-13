from django.db import models

class Topic(models.Model):
    """"User Topic"""
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        """Return presentation of models"""
        return self.text


class Entry(models.Model):
    """Information about learning"""
 #   topic = models.ForeignKey(Topic, on_delete=models.CASCADE,)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """Return presentation of models"""
        return self.text[:50] + "..."
