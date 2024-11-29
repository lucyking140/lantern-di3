from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import os

#for api calls:
import requests
from django.http import JsonResponse

class Profiles(models.Model):
    user = models.OneToOneField(User, default="01", on_delete=models.CASCADE, related_name="profile") #creating profiles
    follows = models.ManyToManyField("self", related_name="followed_by", symmetrical = False, blank = True)
    killCount = models.IntegerField(default = 0)
    profPic = models.ImageField(upload_to='profile_pics', default='fly.webp')
    
    objects = models.Manager()
    
    def __str__(self):
        return self.user.username
        
    def addKill(self): #used whenever a kill is posted
        self.killCount += 1
        self.save()
        
    def get_absolute_url(self):
        return self.profPic.url

#automatically creating a profile for a user when they join
def create_profile(sender, instance, created, **kwargs):
#(**kwargs catches the extra variables that post_save sends
    profile = None
    if created:
        print("making a profile for a created user")
        profile = Profiles.objects.create(user = instance)
        profile.save()
    
    return profile

post_save.connect(create_profile, sender=User) #whenever User implements .save(), this will also implement create_profile


class Kill(models.Model):

    #getting the IP address used in the API call below
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


    user = models.ForeignKey(User, related_name = "kills", on_delete = models.DO_NOTHING)
    image = models.ImageField(upload_to = 'kills', default = 'empty_post.jpg')
    caption = models.CharField(max_length=140)
    posted_time = models.DateTimeField(auto_now_add=True)

    #adding location for the kill, from the Google places API
    api_key = os.environ.get('GMAPS_API_KEY')

    #first getting long/lat
    url = 'https://www.googleapis.com/geolocation/v1/geolocate'
    params = {
        'key': api_key,
        "considerIp": "true",
    }
    response = requests.post(url, params=params)
    geo_data = response.json()
    city = ""
    state = ""
    if "location" in geo_data.keys():
        lat = geo_data["location"]["lat"]
        long = geo_data["location"]["lng"]

        #then getting city from that info
        url = 'https://maps.googleapis.com/maps/api/geocode/json'
        params = {
            'latlng': f'{lat},{long}',
            'key': api_key,
        }
        response = requests.get(url, params=params)
        addr_data = response.json()

        #getting city and state
        for component in addr_data["results"][0]["address_components"]:
            if 'locality' in component['types']:
                city = component['long_name']
            elif 'administrative_area_level_1' in component['types']:
                state = component['long_name']  
            #have already covered both parts
            if state and city:
                break
    else:
        city = "Sorry, no location available"


    def __str__(self): #changing the generic way that a post is displayed
        return(
            f"{self.user}"
            f"({self.posted_time:%Y-%m-%d %H:%M}): "
            f"{self.caption[:15]}..."
            f"{self.city}"
            f"{self.state}"
        )
