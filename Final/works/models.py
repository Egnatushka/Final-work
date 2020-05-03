from django.db import models
from django.shortcuts import reverse



# Create your models here.
class Work(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='work_photo/')
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('works_detail_url', kwargs={'works_ex_id': self.id})

    def __str__(self):
        return self.title



class Order(models.Model):
    customer = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    adress = models.CharField(max_length=250)
    description = models.TextField()
    tag = models.ManyToManyField('Tag', blank=True, related_name='orders')

    def get_absolute_url(self):
        return reverse('order_detail_url', kwargs={'order_id': self.id})

    def get_update_url(self):
        return reverse('order_update_url', kwargs={'order_id': self.id})

    def __str__(self):
        return self.customer




class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title