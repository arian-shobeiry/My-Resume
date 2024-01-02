from django.db import models

# Create your models here.

class music(models.Model):
    title=models.CharField(max_length=100,null=True)
    artist=models.CharField(max_length=100,null=True)
    cover=models.ImageField(upload_to="media/",null=True)
    link=models.CharField(max_length=500,null=True)
    def __str__(self):
        return f'{self.artist} - {self.title}'


class site(models.Model):
    title=models.CharField(max_length=100,null=True)
    image=models.ImageField(upload_to="media/site/")
    sample=models.FileField(upload_to="media/sample/",null=True)
    desc=models.TextField(null=True)
    def __str__(self):
        return f'{self.title}'



class inbox(models.Model):
    name=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    user_message=models.TextField(null=True)
    date=models.CharField(max_length=100,null=True)
    def __str__(self):
        return f"{self.name}"