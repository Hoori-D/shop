from django import forms

from user_profile.models import Profile



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']