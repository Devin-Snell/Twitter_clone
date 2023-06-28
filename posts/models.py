from django.db import models
from cloudinary.models import CloudinaryField

class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
       'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous' 
    )
    body = models.CharField(
       'Body', blank=True, null=False, max_length=140, db_index=True
    )
    created_at = models.DateTimeField(
        'Created DateTime',blank=True, auto_now=True
    )
    likes = models.PositiveIntegerField('likes', default=0, blank = True) 
    image = CloudinaryField('image', blank = True )

    
    def __str__(self):
        return self.body
