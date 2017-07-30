from django import forms
from .models import NewUser
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.models import User

class NewUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = NewUser
        fields = ['email', 'password']

class ChangePasswordForm(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_password2(self, *args, **kwargs):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2:
            if password1!=password2:
                raise forms.ValidationError("Password do not match")
        return password2


class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    # def clean(self, *args, **kwargs):
    #     email = self.cleaned_data.get('email')
    #     password = self.cleaned_data.get('password')
    #     if email and password:
    #         # user = authenticate(username=email, password=password)
    #         user_qs = User.objects.filter(username=email)
    #         # print user_qs
    #         if user_qs.count()==1:
    #             user = user_qs.first()
    #             print user
    #             if not user:
    #                 raise forms.ValidationError("User does not exists")
    #             if not user.check_password(password):
    #                 raise forms.ValidationError("Incorrect password")
    #             if not user.is_active:
    #                 raise forms.ValidationError("Inactive user")
    #     return super(UserLoginForm, self).clean(*args, **kwargs)
