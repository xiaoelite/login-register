'''
@Author: your name
@Date: 2020-03-01 06:18:58
@LastEditTime: 2020-03-03 21:09:34
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /mysite/login/admin.py
'''
from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.User)
admin.site.register(models.ConfirmString)
