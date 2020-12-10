from django import forms
from django.forms.widgets import DateInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from recipe.models import Profile, Post

class UserForm(UserCreationForm):
    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password1 != password2:
            raise forms.ValidationError("Your passwords do not match")
        return password2

    email = forms.CharField(max_length=75, required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('dob', 'picture','firstname','lastname','bio')
        labels = {
        'dob': ('Date of Birth'),
        'firstname':('First Name'),
        'lastname' : ('Last Name'),
        'bio' : ('Biography')
        }
        widgets = {
            'dob': DateInput(attrs={'type': 'date'})
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content','picture', 'category')
        labels = {
            'title': ('Title'),
            'content': ('Your Post Text'),
            'picture': ('Your Post Picture'),
            'category': ('Tag your post category'),
        }

