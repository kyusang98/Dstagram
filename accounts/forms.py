from django.contrib.auth.models import User
from django import forms

'''
python manage.py migrate과정에서 
django.core.exceptions.FieldError: Unknown field(s) (Username) specified for User에러가 발생

fields =['Username', 'first_name', 'last_name', 'email']이라고 되어있었다.
Username -> username으로 수정!!

'''


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password not matched!')
        return cd['password2']
