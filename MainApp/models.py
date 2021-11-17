from django.db import models

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Entry(models.Model):   #has fields called topic, text, and date_added
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
        #allows us to set a special attribute telling Django to use entries
        #when it's referring to multiple entries
    
    def __str__(self):
        return f"{self.text[:50]}..."  #changes the title from "Entry 1" to a short description

