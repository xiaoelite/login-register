'''
@Author: your name
@Date: 2020-03-01 16:59:22
@LastEditTime: 2020-03-02 16:46:49
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /mysite/login/forms.py
'''

from django import forms
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'请输入用户名', 'autofocus':''}))
    password = forms.CharField(label='密码', max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码' }))
    captcha = CaptchaField(label='验证码')


class RegisterForm(forms.Form):
    gender = (
        ('male', '男'),
        ('female', '女'),
    )
    username = forms.CharField(label='用户名', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': '', 'placeholder': '请输入用户名'}))
    password1 = forms.CharField(label='密码', max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'}))
    password2 = forms.CharField(label='确认密码', max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请再次输入密码'}))
    email = forms.EmailField(label='邮箱地址', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    captcha = CaptchaField(label='验证码')

