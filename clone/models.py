from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    photo = CloudinaryField('image')
    bio = models.CharField(max_length=40)
    owner = models.OneToOneField(User,blank=True, on_delete=models.CASCADE, related_name="profile")
    
    
    @classmethod
    def get_all(cls):
        loc = Profile.objects.all()
        return loc
    
    def __str__(self):
        return self.name
    
    
    
class Image(models.Model):
    image = CloudinaryField('image')
    user = models.ForeignKey(User,blank=True, on_delete=models.CASCADE)
    imageName= models.CharField(max_length=70)
    imageCaption= models.TextField()
    profile= models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    pub_date= models.DateTimeField(auto_now_add=True)
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.imageName
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
    
    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images
    


# class Preference(models.Model):
#     user= models.ForeignKey(User, on_delete=models.CASCADE)
#     post= models.ForeignKey(Image, on_delete=models.DO_NOTHING)
#     value= models.IntegerField()
#     date= models.DateTimeField(auto_now_add = True)

    
#     def __str__(self):
#         return str(self.user) + ':' + str(self.post) +':' + str(self.value)

#     class Meta:
#        unique_together = ("user", "post", "value")
       
       
# class Comment(models.Model):
#     image = models.ForeignKey(Image,blank=True, on_delete=models.CASCADE,related_name='comment')
#     comment_owner = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
#     comment= models.TextField()

#     def save_comment(self):
#         self.save()

#     def delete_comment(self):
#         self.delete()

#     @classmethod
#     def get_image_comments(cls, id):
#         comments = Comment.objects.filter(image__pk=id)
#         return comments

#     def __str__(self):
#         return str(self.comment)
