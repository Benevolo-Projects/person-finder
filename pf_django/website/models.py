from django.db import models


class Uploader(models.Model):
    fname_u = models.CharField(max_length=200)
    lname_u = models.CharField(max_length=200)
    email_u = models.EmailField()
    mobile_u = models.IntegerField()
    image_l = models.ImageField(null=True, blank=True)
    #image of uploader

    def __str__(self):
        return self.fname_u + ' ' + self.lname_u


#class Finder(models.Model):
    #input image for finder