from django.db import models

# Create your models here.


class Channel(models.Model):

    def __str__(self) -> str:
        return self.name


    name = models.CharField(default=None, max_length=100)
    url = models.CharField(default=None, max_length=100)


class Video(models.Model):

    def __str__(self) -> str:
        return str(self.title)
    
    id_social = models.CharField(max_length=300, unique=True)
    channel = models.ForeignKey(Channel, on_delete=models.RESTRICT)
    title = models.CharField(default=None, max_length=500)
    url = models.CharField(default=None, max_length=1000)
    thumb = models.CharField(default=None, max_length=1000)
    description = models.CharField(default=None, max_length=5000)

class Comments(models.Model):
    def __str__(self) -> str:
        return self.id.__str__()
    video = models.ForeignKey(Video, on_delete=models.RESTRICT)
    comment=models.CharField(max_length=1000, default=None)