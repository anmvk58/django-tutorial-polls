from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MsbRegisterForm(UserCreationForm):
    username = forms.CharField(label='Tên đăng nhập', required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control form-control-lg msb_input'}))
    email = forms.EmailField(label='Địa chỉ email', required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control form-control-lg msb_input'}))
    first_name = forms.CharField(label='Tên', required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control form-control-lg msb_input'}))
    last_name = forms.CharField(label='Họ và tên đệm', required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control form-control-lg msb_input'}))
    password1 = forms.CharField(label='Mật khẩu', required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg msb_input'}))
    password2 = forms.CharField(label= 'Nhập lại mật khẩu', required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg msb_input'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
