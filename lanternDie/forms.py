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

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',) #adding an email form to the standard Django user model
        
        def save(self, commit = False): #custom save method to hash the password a user enters for their account
            instance = super(CustomUserCreationForm, self).save(commit=False) # create but don't save yet
            if commit:
                instance.set_password(instance.password)
                instance.save()
            return instance

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(required = True, widget = forms.widgets.Textarea(attrs={"placeholder": "thoughts on your kill?", "class": "textarea is-grey is-small",}), label="",)
    email = forms.EmailField(required=True, widget=forms.widgets.Textarea(attrs={"class": "textarea is-grey is-small"}), label = "",)

    class Meta:
        model = Profiles
        fields = ('username', 'email',)

class UpdateProfileForm(forms.ModelForm):
    profPic = forms.ImageField(required = True, label = "",)
    
    class Meta:
        model = Profiles
        fields = ('profPic',)
