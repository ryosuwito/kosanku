from django.contrib.auth.models import User
from django import forms 
from .models import Member

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm,self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()
        self.fields['password'].widget.attrs['placeholder'] = '*********'

    class Meta:
        model = User
        fields = ("username","email","password")

class MemberForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MemberForm,self).__init__(*args, **kwargs)
        self.fields['profile_photo'].widget.attrs['onChange'] = 'Handlechange(event)'
        self.fields['profile_photo'].widget.attrs['class'] = 'hidden'

    class Meta:
        model = Member 
        fields = ("profile_photo","nama_lengkap")
