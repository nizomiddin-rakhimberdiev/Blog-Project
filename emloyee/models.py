# from django.contrib.auth.models import User
# from django.db import models
# from django import forms
#
#
# class Auditable(models.Model):
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=User.pk)
#     created_at = models.TimeField
#     updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=User.pk)
#     updated_at = models.TimeField
#     deleted = models.BooleanField(default=False)
#
#
# class Users(Auditable):
#     user_name = models.CharField(max_length=200)
#     email = models.EmailField(max_length=50)
#     password = forms.CharField(widget=forms.PasswordInput)
#     number = models.IntegerField
#
#
#
#
