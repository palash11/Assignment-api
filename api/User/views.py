from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NewUserForm, UserLoginForm, ChangePasswordForm
from .models import NewUser
from django.views import View
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# from django.contrib.auth.forms import PasswordChangeForm

class UserCBView(View):
    def get(self, request, id):
        instance = get_object_or_404(NewUser, id=id)
        context = {
            "username" : instance.email,
        }
        return render(request, "view_user.html", context)

class RegisterView(CreateView):
    form_class = NewUserForm
    template_name = 'register.html'
    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password = password
        user.save()
        form.save()
        return redirect(user.get_absolute_url())

class LoginView(FormView):
    form_class = UserLoginForm
    template_name = 'login.html'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user_qs = NewUser.objects.filter(email=email).filter(password=password)
        if user_qs.count()==1:
            user = user_qs.first()
            login(self.request, user)
            return redirect('User:new')
        return HttpResponse('Wrong Credentials')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


def new(request):
    return HttpResponse("Login successful")

def change(request):
    return HttpResponse("Password change successful")

@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST or None)
        if form.is_valid:
            if request.user.is_authenticated:
                user = request.user
                password = form['password2']
                user.set_password(password)
                user.save()
                form.save()
                update_session_auth_hash(request, user)
                return redirect('User:done')
        else:
            return redirect('User:password_change')
    else:
        form = ChangePasswordForm()
    context = {"form" : form}
    return render(request, 'change_password.html', context)

# @method_decorator(login_required, name='post')
# class PasswordChangeView(View):
#     def post(self, request):
#         form = PasswordChangeForm(data=request.POST, user = request.user)
#
#         if form.is_valid:
#             form.save()
#             update_session_auth_hash(request, form.user)
#             return redirect('User:done')
#         else:
#             return redirect('User:password_change')
#
#         context = {"form" : form}
#         return render(request, 'change_password.html', context)
