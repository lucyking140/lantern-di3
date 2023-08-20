from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializers import ldSerializer
from .models import Profiles, Kill
from django.views import generic
from django.urls import reverse
from .forms import KillForm, CustomUserCreationForm, UpdateUserForm, UpdateProfileForm
from django.contrib.auth import login

def registration(request):
    if request.method == "GET":
            return render(
                request, "registration/signup.html",
                {"form": CustomUserCreationForm}
            )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        #print("request.FILES: ", request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print("saved user form")
        else:
            print(form.errors)
        #return redirect(reverse("lanternDie:dashboard"))
        return render(request, 'lanternDie/dashboard.html', {'form': form})

def kill_view(request):
    post = get_object_or_404(models.Kill)
    return render(request, "kill.html", locals())

def dashboard(request):
    #form = KillForm() #always generates a blank form even if there is no submission
    return render(request, "lanternDie/dashboard.html")
    
def profile_list(request):
    profiles = Profiles.objects.exclude(user=request.user)
    return render(request, "lanternDie/profile_list.html", {"profiles": profiles})
    
def profile(request, pk):
    profile = Profiles.objects.get(pk = pk) #get call to the database of users
    #profPicUrl = f"https://lanterndi3-heroku.s3.amazonaws.com/ { profile.profPicKey }"
    if request.method == "POST": #idea here is that a user (current user) is on a given profile's (profile) page when they request to follow them, so that form is submitted to the profile view
        print("profile1: ", profile)
        current_user = request.user.profile
        message = request.POST
        result = message.get("follow") #saying which key to get the message from
        print("result: ", result)
        if result == "follow":
            current_user.follows.add(profile)
            print("unfollowing")
        elif result == "unfollow":
            current_user.follows.remove(profile)
            print("following")
        current_user.save()
        print("successfully un/followed user")
    
    return render(request, "lanternDie/profile.html", {"profile": profile})
    
def postKill(request):
    form = KillForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            kill = form.save(commit = False)
            kill.user = request.user
            Profiles.objects.get(user_id = kill.user.id).addKill() #incrementing the user's number of kills
            kill.save()
            return redirect("lanternDie:dashboard") #prevents multiple submissions on resubmit
        else:
            print(form.errors)
    return render(request, "lanternDie/postKill.html", {"form": form})

def changeProf(request):
    user_form = UpdateUserForm(request.POST or None, instance=request.user)
    prof_form = UpdateProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)
    if request.method == 'POST':
        print("is indeed a post")
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            print("successfully changed profile")

            return redirect("lanternDie:dashboard")
        else:
            print(user_form.errors)
            print(prof_form.errors)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'lanternDie/changeProf.html', {'user_form': user_form, 'prof_form': prof_form})
