from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profiles
from .models import Kill
    
class ProfileInline(admin.StackedInline):
   model = Profiles

class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username", "emailaddress", "firstname", "lastname", "staffstatus", "killCount", "profPic"] #these are the default user characteristics
    inlines = [ProfileInline] #registering inline makes the profile info appear under the user info in the admin page
    
class KillAdmin(admin.ModelAdmin):
    model = Kill
    field = ["user", "image", "caption", "posted_time"]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Kill, KillAdmin)
admin.site.register(Profiles)
