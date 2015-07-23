from django.db import models
from django.utils import timezone
import os
# Create your models here.

def get_image_path(person, filename):
    return os.path.join('photos', str(person.person).replace(' ', ''), filename)

class Followers(models.Model):
    follower = models.CharField(max_length=140)
    following = models.NullBooleanField(default=True) 
    
    def approved_warnings(self):
        return self.warnings
    
    def __str__(self):
        return self.follower
    
    
class Warning(models.Model):
    person = models.ForeignKey('yardsale.Followers', related_name='warnings')
    author = models.CharField(max_length=100)
    editor = models.CharField(max_length=100, blank=True, null=True)
    descript = models.TextField(max_length=5000)
    publish_date = models.DateTimeField(blank=True, null=True)
    edited_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    image2 = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    image3 = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    image4 = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    image5 = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    WT1 = 'Bumping'
    WT2 = 'Pet'
    WT3 = 'Business'
    WT4 = 'Outside Links'
    WT5 = 'Price Undefined'
    WT6 = 'Other'
    WARNINGTYPES = (
        (WT1, 'Bumping'),
        (WT2, 'Pet'),
        (WT3, 'Business'),
        (WT4, 'Outside Links'),
        (WT5, 'Price Undefined'),
        (WT6, 'Other'),
    )
    WarningType = models.CharField(max_length=15, choices=WARNINGTYPES, default=WT1)

#     def publishwarning(self):
#         self.author = auth.User()
#         self.publish_date = timezone.now()
#         self.save()
#     
#     def edit(self):
#         editor = auth.User()
#         self.publish_date = timezone.now()
#         self.save()
        
    def __str__(self):
        return self.descript