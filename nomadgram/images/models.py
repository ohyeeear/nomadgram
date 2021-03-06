from django.db import models
from nomadgram.users import models as user_models 

# Create your models here.
class TimeSpampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True 


class Image(TimeSpampedModel):

    """ image model """
    file= models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.CASCADE, related_name='images')
    
    @property
    def like_count(self):
        return self.likes.all().count()

    def __str__(self):
        return '{} - {}'.format(self.location, self.caption)

class Comment(TimeSpampedModel) :
    """ commemnt model """
    message = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, null=True , on_delete=models.CASCADE , related_name='comments')

    def __str__(self):
        return self.message


class Like(TimeSpampedModel) :
    """ like model """
    creator = models.ForeignKey(user_models.User, null=True , on_delete=models.CASCADE)
    image = models.ForeignKey(Image, null=True, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return 'User : {} - {}'.format(self.creator.username, self.image.caption)
