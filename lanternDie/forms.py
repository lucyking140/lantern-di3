from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Kill, Profiles

class KillForm(forms.ModelForm):
    caption = forms.CharField(required = True, widget = forms.widgets.Textarea(attrs={"placeholder": "thoughts on your kill?", "class": "textarea is-grey is-medium",}), label="",)
    image = forms.ImageField(required = True, label = "",)
    class Meta:
        model = Kill
        exclude = ("user", )
        
        
class CustomUserCreationForm(UserCreationForm):
    profPic = forms.ImageField(required = False, label = "profPic",)
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", "profPic",)

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(required = True, widget = forms.widgets.Textarea(attrs={"placeholder": "thoughts on your kill?", "class": "textarea is-grey is-small",}), label="",)
    email = forms.EmailField(required=True,
                             widget=forms.widgets.Textarea(attrs={'class': 'textarea is-grey is-small'}), label = "",)
    profPic = forms.ImageField(required = True, label = "",)

    class Meta:
        model = Profiles
        fields = ('username', 'email', 'profPic')
