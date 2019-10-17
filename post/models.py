from django.db import models
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120, verbose_name= 'Title')
    content = models.TextField(verbose_name= 'Content')
    publishDate = models.DateTimeField(verbose_name= 'Publish Date',auto_now_add=True)

    def __str__(self):
        return self.title

    def getAbsoluteURL(self):
        return reverse('post:detail', kwargs= {'id':self.id})
        # return "/post/{}".format(self.id)

    def getCreateURL(self):
        return reverse('post:create')

    def getUpdateURL(self):
        return reverse('post:update', kwargs= {'id':self.id})

    def getDeleteURL(self):
        return reverse('post:delete', kwargs= {'id':self.id})
