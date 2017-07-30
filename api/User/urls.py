from django.conf.urls import url
from .views import (
    UserCBView,
    RegisterView,
    LoginView,
    new,
    change,
    change_password
    )


urlpatterns = [
    url(r'^users/$', RegisterView.as_view(), name='register'),
    url(r'^users/(?P<id>\d+)/$', UserCBView.as_view(), name='details'),
    url(r'^users/login/$', LoginView.as_view(), name="user_login"),
    url(r'^users/new/$', new, name="new"),
    url(r'^change_password/$', change_password, name='password_change'),
    url(r'^change_password_done/$', change, name='done'),
    url(r'^reset_password/$', change_password, name='reset_password'),
]
