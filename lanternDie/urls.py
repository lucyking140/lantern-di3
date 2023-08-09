from django.urls import path
from .views import dashboard, profile_list, profile, registration, kill_view

app_name = "lanternDie"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"), #this int:pk means that any url with profile/<some integer> will redirect to the profile() view
    path("registration/", registration, name="registration"),
    path("kill/", kill_view, name = "kill")
    
]
