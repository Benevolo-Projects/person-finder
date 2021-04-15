from django.db import models
from django.utils import timezone
import os, glob
from uuid import uuid4

count = 0


def path_and_rename(instance, filename):
    name1 = str(len(glob.glob('../images/db/Known/*')))
    print(name1)
    return os.path.join(name1 + ".jpg")


def rename(instance, filename):
    os.remove('../images/db/Known/Unknown/0.jpg')
    name1 = str(0)
    return os.path.join('./Unknown/' + name1 + ".jpg")


class Uploader(models.Model):
    fname_u = models.CharField(max_length=200)
    lname_u = models.CharField(max_length=200)
    email_u = models.EmailField()
    mobile_u = models.IntegerField()
    image_l = models.ImageField(upload_to=path_and_rename, null=True, blank=True)

    # image of uploader

    def __str__(self):
        return self.fname_u + ' ' + self.lname_u


class Find(models.Model):
    image = models.ImageField(upload_to=rename, null=True, blank=True)


# class Finder(models.Model):
# input image for finder
