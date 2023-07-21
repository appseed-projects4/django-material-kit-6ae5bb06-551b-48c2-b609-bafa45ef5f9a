# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Userprofile(models.Model):

    #__Userprofile_FIELDS__
    address = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zip = models.CharField(max_length=255, null=True, blank=True)

    #__Userprofile_FIELDS__END

    class Meta:
        verbose_name        = _("Userprofile")
        verbose_name_plural = _("Userprofile")


class (models.Model):

    #___FIELDS__

    #___FIELDS__END

    class Meta:
        verbose_name        = _("")
        verbose_name_plural = _("")


class Motorcycle(models.Model):

    #__Motorcycle_FIELDS__
    make = models.CharField(max_length=255, null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    year = models.CharField(max_length=255, null=True, blank=True)
    license = models.CharField(max_length=255, null=True, blank=True)

    #__Motorcycle_FIELDS__END

    class Meta:
        verbose_name        = _("Motorcycle")
        verbose_name_plural = _("Motorcycle")



#__MODELS__END
