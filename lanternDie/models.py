from django.db import models
from django.contrib.auth.models import User
#from django.db.models.signals import post_save

class Profiles(models.Model):
    user = models.OneToOneField(User, default="01", on_delete=models.CASCADE, related_name="profile") #creating profiles
    follows = models.ManyToManyField("self", related_name="followed_by", symmetrical = False, blank = True)
    killCount = models.IntegerField(default = 0)
    profPic = models.ImageField(upload_to='profile_pics', default='fly.webp')
    #profPicKey = models.CharField(default = 'fly', max_length = 500) #setting the s3 url for the specific file
    
    objects = models.Manager()
    
    def __str__(self):
        return self.user.username
        
    def addKill(self): #used whenever a kill is posted
        self.killCount += 1
        self.save()
        
    def get_absolute_url(self):
        return self.profPic.url
'''
#automatically creating a profile for a user when they join
def create_profile(sender, instance, created, **kwargs):
#(**kwargs catches the extra variables that post_save sends -- can make this better later
    profile = None
    if created:
        print("making a profile for a created user")
        profile = Profiles.objects.create(user = instance)
        profile.save()
    
    return profile
post_save.connect(create_profile, sender=User) #whenever User implements .save(), this will also implement create_profile
'''
#look into decorators to make this part more streamlined

class Kill(models.Model):
    user = models.ForeignKey(User, related_name = "kills", on_delete = models.DO_NOTHING)
    image = models.ImageField(upload_to = 'kills', default = 'empty_post.jpg')
    caption = models.CharField(max_length=140)
    posted_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self): #changing the generic way that a post is displayed
        return(
            f"{self.user}"
            f"({self.posted_time:%Y-%m-%d %H:%M}): "
            f"{self.caption[:15]}..."
        )
