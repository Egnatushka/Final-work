from django.db import models

# Create your models here.
class Work(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='work_photo/')
    description = models.TextField()



    def __str__(self):
        return self.title
