from django.contrib.auth.models import User
from django import forms

def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력하세요.')


class CommentForm(forms.Form):
    comment = forms.CharField(validators=[min_length_3_validator])
    movie = forms.CharField()


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput({"placeholder": "아이디"}))
    email = forms.CharField(widget=forms.TextInput({"placeholder": "이메일"}))
    password = forms.CharField(widget=forms.PasswordInput({"placeholder": "비밀번호"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']



class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput({"placeholder": "아이디"}))
    password = forms.CharField(widget=forms.PasswordInput({"placeholder": "비밀번호"}))

    class Meta:
        model = User
        fields = ['username', 'password']
