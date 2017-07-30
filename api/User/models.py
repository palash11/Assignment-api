from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
import datetime

class NewUser(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    last_login = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("User:details", kwargs={"id" : self.id})
