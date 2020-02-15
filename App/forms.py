from django.forms import ModelForm
from App.models import User
from django import forms


from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ("username", "first_name","last_name","email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        print(self.cleaned_data["username"])
        print(self.cleaned_data["email"])
        user.first_name = self.cleaned_data["first_name"]
        print(self.cleaned_data["first_name"])
        user.last_name = self.cleaned_data["last_name"]
        print(self.cleaned_data["last_name"])


        if commit:
            user.save()
        return user