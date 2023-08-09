from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Kill

class KillForm(forms.ModelForm):
    caption = forms.CharField(required = True, widget = forms.widgets.Textarea(attrs={"placeholder": "thoughts on your kill?", "class": "textarea is-grey is-medium",}), label="",)
    image = forms.ImageField(required = True, label = "",)
    class Meta:
        model = Kill
        exclude = ("user", )
        
        
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
