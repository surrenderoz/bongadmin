from django.db import models
# Create your models here.
class CreateArtist(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    bday = models.CharField(max_length=20)
    emailid = models.EmailField(max_length=30)
    gender = models.CharField(max_length=20)
    bio = models.TextField(max_length=100)
    profileimg = models.ImageField(upload_to="image/")
    awards = models.CharField(max_length=30)
    websiteurl = models.URLField(max_length=30)
    genre = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    createdon = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(True)


class TestCreate(models.Model):
    name = models.CharField(max_length=50)
    data = models.CharField(max_length=50)
    cold = models.CharField(max_length=50)
    images = models.ImageField(upload_to="images/")
    