from django.urls import path
from .views import dashboard, profile_list, profile, registration, kill_view, postKill, changeProf
from django.contrib.auth import views as auth_views

app_name = "lanternDie"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"), #int:pk so that any url with profile/<some integer> will redirect to the profile() view
    path("registration/", registration, name="registration"),
    path("kill/", kill_view, name = "kill"),
    path("postKill/", postKill, name = "postKill"),
    path("changeProf/", changeProf, name = "changeProf"),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name = 'lanternDie/change_password.html', success_url = '/'), name = "change_password"),
]
