from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializers import ldSerializer
from .models import Profiles, Kill
from django.views import generic
from django.urls import reverse
from .forms import KillForm, CustomUserCreationForm
from django.contrib.auth import login

def registration(request):
    if request.method == "GET":
            return render(
                request, "registration/signup.html",
                {"form": CustomUserCreationForm}
            )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("lanternDie:dashboard"))

def kill_view(request):
    post = get_object_or_404(models.Kill)
    return render(request, "kill.html", locals())

def dashboard(request):
    form = KillForm(request.POST or None, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            kill = form.save(commit = False)
            kill.user = request.user
            Profiles.object.get(user_id = kill.user.id).addKill() #incrementing the user's number of kills
            kill.save()
            return redirect("lanternDie:dashboard") #prevents multiple submissions on resubmit
        else:
            print(form.errors)
    #form = KillForm() #always generates a blank form even if there is no submission
    return render(request, "lanternDie/dashboard.html", {"form": form})
    
def profile_list(request):
    profiles = Profiles.object.exclude(user=request.user)
    return render(request, "lanternDie/profile_list.html", {"profiles": profiles})
    
def profile(request, pk):
    profile = Profiles.object.get(pk = pk) #get call to the database of users
    if request.method == "POST": #idea here is that a user (current user) is on a given profile's (profile) page when they request to follow them, so that form is submitted to the profile view
        print("profile: ", profile)
        current_user = request.user.profile
        message = request.POST
        result = message.get("follow") #saying which key to get the message from
        if result == "follow":
            current_user.follows.remove(profile)
        elif result == "unfollow":
            current_user.follows.add(profile)
        current_user.save()
        print("successfully un/followed user")
    return render(request, "lanternDie/profile.html", {"profile": profile})
