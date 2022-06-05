from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=40)
    
    @classmethod
    def get_all(cls):
        loc = Location.objects.all()
        return loc
    
    def __str__(self):
        return self.name
    
    
    
class Image(models.Model):
    image = CloudinaryField('image')
    imageOwner = models.ForeignKey(User, on_delete=models.DO_NOTHING,)
    imageName= models.CharField(max_length=70)
    imageDescription= models.TextField()
    imageLocation= models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    pub_date= models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.imageName
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
    
    
    