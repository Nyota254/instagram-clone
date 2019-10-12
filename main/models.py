from django.db import models
from django.contrib.auth.models import User


class Like(models.Model):
    '''
    This model will contain the columns to our likes class
    '''
    like = models.IntegerField(blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Comment(models.Model):
    '''
    This model will contain the columns for our comments class
    '''
    comment = models.CharField(max_length=250)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Image(models.Model):
    '''
    This model will contain the columns to our image class
    '''
    image = models.ImageField(upload_to='main_photos/')
    image_name = models.CharField(max_length=30)
    image_caption=models.CharField(max_length=300,blank=True)
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    likes = models.ForeignKey(Like,on_delete=models.CASCADE,blank=True)
    comments = models.ForeignKey(Comment,on_delete=models.CASCADE,blank=True)

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




