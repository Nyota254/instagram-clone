from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    '''
    This model will contain the columns to our image class
    '''
    image = models.ImageField(upload_to='main_photos/')
    image_name = models.CharField(max_length=30)
    image_caption=models.CharField(max_length=300,blank=True)
    profile = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name

    @classmethod
    def save_image(self):
        '''
        Saves an Image in the db
        '''
        self.save()

    @classmethod
    def delete_image(self):
        '''
        Deletes an image model from the db
        '''
        self.delete()

    @classmethod
    def update_caption(self):
        '''
        Saves a caption from the db
        '''
        pass



class Likes(models.Model):
    '''
    This model will contain the columns to our likes class
    '''
    image_like = models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    
    def __int__(self):
        return self.like


class Comment(models.Model):
    '''
    This model will contain the columns for our comments class
    '''
    comment = models.CharField(max_length=255,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)

    def __str__(self):
        return self.comment





