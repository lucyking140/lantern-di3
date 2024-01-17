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
        form = CustomUserCreationForm(request.POST)
        #print("request.FILES: ", request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print("saved user form")
            return render(request, 'lanternDie/dashboard.html', {'form': form})
           
        else:
            print(form.errors)
            return render(request, 'registration/signup.html', {'form': form})
    
        

def kill_view(request):
    post = get_object_or_404(models.Kill)

    return render(request, "kill.html", locals())

def dashboard(request):
    
    #re-ordering all posts from all users that a profile follows:
    
    user = request.user # Assuming you have authenticated users
    ordered_posts = []
    posts = []

    if user.is_authenticated:
        follows = user.profile.follows.all()

        for followed in follows:
            posts.extend(followed.user.kills.all())
            
        posts.extend(user.kills.all()) #including the user's own posts
    else: #if not an account, just show all posts
        for users in Profiles.objects.all():
            posts.extend(users.user.kills.all())
        
    ordered_posts = sorted(posts, key=lambda x: x.posted_time, reverse=True)
    
    return render(request, "lanternDie/dashboard.html", {'ordered_posts': ordered_posts,})
    
def profile_list(request):
    profiles = Profiles.objects.exclude(user=request.user)
    return render(request, "lanternDie/profile_list.html", {"profiles": profiles})
    
def profile(request, pk):
    profile = Profiles.objects.get(pk = pk) #get call to the database of users
    
    current_user = request.user
    current_prof = request.user.profile
    
    all_profs = Profiles.objects.all()
    all_users = []
    for prof in all_profs:
        all_users.append(prof.user)
    
    posts = profile.user.kills.all()
    
    #making the list of the user's posts chronological
    ordered_kills = sorted(posts, key=lambda x: x.posted_time, reverse=True)
    
    #following/unfollowing
    if request.method == "POST": #idea here is that a user (current user) is on a given profile's (profile) page when they request to follow them, so that form is submitted to the profile view
        message = request.POST
        result = message.get("follow") #saying which key to get the message from
        print("result: ", result)
        if result == "follow":
            current_prof.follows.add(profile)
            print("unfollowing")
        elif result == "unfollow":
            current_prof.follows.remove(profile)
            print("following")
        current_prof.save()
        print("successfully un/followed user")
        
    
    return render(request, "lanternDie/profile.html", {"profile": profile, "ordered_kills": ordered_kills, "all_profs": all_profs})
    
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
